import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import pyperclip
import arxiv_fetch.arxiv_fetch as arxiv_fetch
import arxiv_gui.arxiv_gui as arxiv_gui  # Add this line to import the arxiv_gui module

def search_button_click():
    query = arxiv_gui.get_query()
    max_results = arxiv_gui.get_max_results()
    papers = arxiv_fetch.fetch_arxiv_papers(query, max_results)
    arxiv_gui.display_results(papers)

def save_to_file():
    results = arxiv_gui.get_results()
    arxiv_gui.save_to_file(results)

def copy_citations():
    bibtex_citations = arxiv_gui.get_bibtex_citations()
    pyperclip.copy("\n\n".join(bibtex_citations))
    messagebox.showinfo("Success", "BibTeX citations copied to clipboard.")

if __name__ == "__main__":
    app = tk.Tk()
    app.title("ArXiv Papers Search")

    arxiv_gui.create_widgets(app, search_button_click, save_to_file, copy_citations)

    app.mainloop()

