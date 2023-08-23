"""
This script extracts content from a Jupyter Notebook (in .ipynb format) and 
generates a Markdown (in .md format) with a Table of Contents. It also organizes
the content based on the headers in the notebook and provides a slugified link 
for easy navigation.

Author: David van der Byl

TODO: add plot/figure extraction
"""

import os
import nbformat
import re
import unicodedata

def slugify(value):
    """
    Convert a string to a URL-friendly slug.
    
    Inputs:
    - value (str): String to be converted to slug.
    
    Outputs:
    - str: Slugified string.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value

def extract_headers_and_content(notebook):
    """
    Extract headers and content from the notebook cells.
    
    Inputs:
    - notebook (nbformat.NotebookNode): Notebook object parsed by nbformat.
    
    Outputs:
    - tuple: Title of the notebook (str), list of tuples containing header and corresponding content.
    """
    headers_and_content = []
    current_header = None
    current_content = ""
    title = None

    # Loop through each cell in the notebook
    for cell in notebook.cells:
        # If the cell type is Markdown
        if cell.cell_type == 'markdown':
            # Split content by headers
            blocks = re.split(r'^(#+\s+.*)$', cell.source, flags=re.MULTILINE)
            for block in blocks:
                block = block.strip()
                if not block:
                    continue
                # Check if block is a header
                if re.match(r'^#+\s+', block):
                    # If it's the first level-1 header, set it as the title
                    if title is None and re.match(r'^#\s+', block):
                        title = block
                        continue
                    # Skip old table of contents headers
                    if 'table of contents' in block.lower():
                        continue
                    # If a header is already being tracked, append it and its content
                    if current_header:
                        headers_and_content.append((current_header, current_content.strip()))
                    current_header = block
                    current_content = ""
                else:
                    # Add block to current content
                    current_content += "\n" + block
        # If the cell is a code cell
        elif cell.cell_type == 'code':
            current_content += "\n```python\n" + cell.source + "\n```\n"
    
    # After all cells are processed, add any remaining header and content
    if current_header:
        headers_and_content.append((current_header, current_content.strip()))

    return title, headers_and_content

def generate_table_of_contents(headers_and_content, toc_level=2):
    """
    Generate a table of contents based on the list of headers and content.
    
    Inputs:
    - headers_and_content (list): List of tuples containing headers and their content.
    - toc_level (int): Depth of headers to include in the table of contents.
    
    Outputs:
    - str: Table of Contents in Markdown format.
    """
    toc = "## Table of Contents\n"
    for i, (header, _) in enumerate(headers_and_content, 1):
        header_level = len(re.findall(r'^#+', header)[0])
        header_text = re.findall(r'^#+\s+(.*)', header)[0]

        if header_level <= toc_level:
            link = slugify(header_text)
            indentation = '  ' * (header_level - 1)
            toc += f"{indentation}- [{header_text}](#{link})\n"
        
    return toc

def generate_markdown_with_toc(ipynb_file_path, toc_level=2, md_file_path=None):
    """
    Convert a Jupyter Notebook to a Markdown file with a Table of Contents.
    
    Inputs:
    - ipynb_file_path (str): Path to the Jupyter Notebook (.ipynb) file.
    - toc_level (int): Depth of headers to include in the table of contents.
    - md_file_path (str, optional): Desired path for the output Markdown file. 
      Defaults to same location and name as the input file, but with .md extension.
    
    Outputs:
    None. A Markdown file will be written to the given or default path.
    """
    try:
        notebook = nbformat.read(ipynb_file_path, as_version=nbformat.NO_CONVERT)
        title, headers_and_content = extract_headers_and_content(notebook)
        toc = generate_table_of_contents(headers_and_content, toc_level)

        if md_file_path is None:
            md_file_path = os.path.splitext(ipynb_file_path)[0] + ".md"

        with open(md_file_path, 'w') as md_file:
            if title:
                md_file.write(f"{title}\n\n")
            md_file.write(toc)
            for header, content in headers_and_content:
                md_file.write(f"\n{header}\n")
                md_file.write(content)

        print(f"Table of Contents and content generated successfully and saved to: {md_file_path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ipynb_file_path = "/Users/davidvanderbyl/Documents/GitHub/Data_Science_Handbooks/Python Tutorial Handbook for Data Science.ipynb"  # Replace with the actual file path
    toc_level = 2  # Change to 1, 2, 3, etc., to include headers of different levels in the toc
    # Use the default behavior to generate .md file in the same directory as the .ipynb file
    generate_markdown_with_toc(ipynb_file_path, toc_level)
