# Import the required modules from the tkinter library.
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Import the pyperclip module to enable copying to the clipboard.
import pyperclip

# Import the arxiv_fetch and arxiv_gui modules. The arxiv_fetch module contains the function to fetch arXiv papers,
# and the arxiv_gui module contains the GUI-related functions and widgets.
import arxiv_fetch.arxiv_fetch as arxiv_fetch
import arxiv_gui.arxiv_gui as arxiv_gui

# Function to be called when the "Search" button is clicked.
def search_button_click():
    # Get the user input query and maximum number of results from the arxiv_gui module.
    query = arxiv_gui.get_query()
    max_results = arxiv_gui.get_max_results()
    
    # Fetch arXiv papers based on the provided query and maximum number of results.
    papers = arxiv_fetch.fetch_arxiv_papers(query, max_results)
    
    # Display the fetched papers in the GUI using the arxiv_gui module.
    arxiv_gui.display_results(papers)

# Function to be called when the "Save to File" button is clicked.
def save_to_file():
    # Get the search results from the arxiv_gui module.
    results = arxiv_gui.get_results()
    
    # Save the search results to a file named "arxiv_papers.txt" using the arxiv_gui module.
    arxiv_gui.save_to_file(results)

# Function to be called when the "Copy Citations to Clipboard" button is clicked.
def copy_citations():
    # Get the BibTeX citations from the search results using the arxiv_gui module.
    bibtex_citations = arxiv_gui.get_bibtex_citations()
    
    # Copy the BibTeX citations to the clipboard using the pyperclip module.
    # The citations are joined with two newline characters for better separation.
    pyperclip.copy("\n\n".join(bibtex_citations))
    
    # Display a success message using a messagebox from the tkinter library.
    messagebox.showinfo("Success", "BibTeX citations copied to clipboard.")

# The __name__ variable will be "__main__" only if this script is being executed directly.
# If the script is imported as a module, the __name__ variable will have a different value.
if __name__ == "__main__":
    # Create the main application window using the tkinter library.
    app = tk.Tk()
    app.title("ArXiv Papers Search")  # Set the title of the application window.

    # Call the create_widgets function from the arxiv_gui module to set up the GUI widgets.
    # Pass the required functions (search_button_click, save_to_file, copy_citations) to handle button clicks.
    arxiv_gui.create_widgets(app, search_button_click, save_to_file, copy_citations)

    # Start the main event loop of the application to handle user interactions and display the GUI.
    app.mainloop()

