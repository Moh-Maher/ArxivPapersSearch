# Import the arxiv module to access the arXiv API.
import arxiv

# Function to fetch arXiv papers based on a query and return the results as a list of dictionaries.
def fetch_arxiv_papers(query, max_results=10):
    # Perform a search on arXiv using the provided query and other parameters.
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    # Initialize an empty list to store the fetched papers.
    papers = []

    # Loop through the search results and extract relevant information for each paper.
    for result in search.results():
        # Create a list of authors' names from the authors' objects in the result.
        authors_list = [author.name for author in result.authors]
        # Combine the authors' names into a single string, separated by 'and' for proper formatting.
        authors = " and ".join(authors_list)
        # Convert the publication date into a formatted string (YYYY-MM-DD).
        published_date = result.published.strftime("%Y-%m-%d")
        # Create a BibTeX citation for the paper using the extracted information.
        bibtex_citation = f"@article{{{result.entry_id},\n" \
                          f"    author = {{{authors}}},\n" \
                          f"    title = {{{result.title}}},\n" \
                          f"    journal = {{arXiv preprint arXiv:{result.entry_id}}},\n" \
                          f"    year = {{{published_date}}}\n" \
                          f"}}"
        # Create a dictionary containing various details of the paper and add it to the list.
        papers.append({
            "title": result.title,
            "authors": authors,
            "abstract": result.summary,
            "published_date": published_date,
            "doi": result.doi,
            "pdf_url": result.pdf_url,
            "bibtex_citation": bibtex_citation
        })

    # Return the list of dictionaries containing information about the fetched papers.
    return papers

