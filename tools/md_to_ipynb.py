# Import necessary libraries
import os
import json
from markdown_it import MarkdownIt
from markdown_it.token import Token
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import notedown
import nbformat

def md_to_ipynb(md_file_path):
    """
    Converts a Markdown file to a Jupyter notebook.

    Parameters:
    md_file_path (str): The path to the Markdown file to convert.

    Returns:
    None
    """

    # Read the markdown file's content
    with open(md_file_path, 'r') as f:
        markdown_string = f.read()

    # Use notedown to convert the markdown string to a Jupyter notebook
    reader = notedown.MarkdownReader()
    notebook = reader.reads(markdown_string)

    # Define path for the Jupyter notebook file
    ipynb_file_path = os.path.splitext(md_file_path)[0] + '.ipynb'

    # Write the Jupyter notebook to a file
    with open(ipynb_file_path, 'w') as f:
        nbformat.write(notebook, f)


def main(input_path): 
    md_to_ipynb(input_path)

# If this script is being run directly (as opposed to being imported), parse command line arguments and call the main function.
if __name__ == "__main__":
    input_path = '/Users/davidvanderbyl/Documents/GitHub/Data_Science_Handbooks/SQL Database Tutorial Handbook.md'
    main(input_path)
