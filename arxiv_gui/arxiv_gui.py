# Import the required modules from the tkinter library.
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Define the entry_query as a global variable in the module to access it across functions.
entry_query = None

# Function to create and display the widgets in the application.
def create_widgets(app, search_button_click, save_to_file, copy_citations):
    global entry_query, entry_max_results, results_text  # Reference the global variables

    # Create and pack the "Query:" label and input field for user input.
    label_query = tk.Label(app, text="Query:")
    label_query.pack()

    entry_query = tk.Entry(app, width=50)
    entry_query.pack()

    # Create and pack the "Max Results:" label and input field for user input.
    label_max_results = tk.Label(app, text="Max Results:")
    label_max_results.pack()

    entry_max_results = tk.Entry(app, width=10)
    entry_max_results.pack()

    # Create and pack the "Search" button, which will execute the search_button_click function when clicked.
    search_button = tk.Button(app, text="Search", command=search_button_click)
    search_button.pack()

    # Create and pack the scrolled text widget to display the search results.
    results_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=20)
    results_text.pack()

    # Create and pack the "Save to File" button, which will execute the save_to_file function when clicked.
    save_button = tk.Button(app, text="Save to File", command=save_to_file)
    save_button.pack()

    # Create and pack the "Copy Citations to Clipboard" button, which will execute the copy_citations function when clicked.
    copy_button = tk.Button(app, text="Copy Citations to Clipboard", command=copy_citations)
    copy_button.pack()

# Function to retrieve the user input query from the Entry widget.
def get_query():
    return entry_query.get()

# Function to retrieve the user input maximum number of results from the Entry widget.
def get_max_results():
    return int(entry_max_results.get())

# Function to display the search results in the scrolled text widget.
def display_results(papers):
    results_text.delete(1.0, tk.END)
    for paper in papers:
        results_text.insert(tk.END, "=" * 80 + "\n")
        results_text.insert(tk.END, f"Title: {paper['title']}\n")
        results_text.insert(tk.END, f"Authors: {paper['authors']}\n")
        results_text.insert(tk.END, f"Abstract: {paper['abstract']}\n")
        results_text.insert(tk.END, f"Published Date: {paper['published_date']}\n")
        results_text.insert(tk.END, f"DOI: {paper['doi']}\n")
        results_text.insert(tk.END, f"PDF URL: {paper['pdf_url']}\n")
        results_text.insert(tk.END, "=" * 80 + "\n")
        results_text.insert(tk.END, f"BibTeX Citation:\n{paper['bibtex_citation']}\n\n")

# Function to retrieve the search results from the scrolled text widget.
def get_results():
    return results_text.get(1.0, tk.END)

# Function to save the search results to a file named "arxiv_papers.txt".
def save_to_file(results):
    with open("arxiv_papers.txt", "w", encoding="utf-8") as file:
        file.write(results)
    messagebox.showinfo("Success", "Results have been saved to arxiv_papers.txt")

# Function to extract BibTeX citations from the search results.
def get_bibtex_citations():
    results = results_text.get(1.0, tk.END)
    bibtex_citations = []
    while True:
        start = results.find("@article{")
        end = results.find("}", start)
        if start == -1 or end == -1:
            break
        bibtex_citations.append(results[start:end + 1])
        results = results[end + 1:]
    return bibtex_citations

