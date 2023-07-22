import arxiv

def fetch_arxiv_papers(query, max_results=10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in search.results():
        authors_list = [author.name for author in result.authors]
        authors = " and ".join(authors_list)
        published_date = result.published.strftime("%Y-%m-%d")
        bibtex_citation = f"@article{{{result.entry_id},\n" \
                          f"    author = {{{authors}}},\n" \
                          f"    title = {{{result.title}}},\n" \
                          f"    journal = {{arXiv preprint arXiv:{result.entry_id}}},\n" \
                          f"    year = {{{published_date}}}\n" \
                          f"}}"
        papers.append({
            "title": result.title,
            "authors": authors,
            "abstract": result.summary,
            "published_date": published_date,
            "doi": result.doi,
            "pdf_url": result.pdf_url,
            "bibtex_citation": bibtex_citation
        })

    return papers

