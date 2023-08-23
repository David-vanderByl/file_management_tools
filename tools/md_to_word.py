"""
Script Name: md_to_word.py
Author: OpenAI
Date: 28th July 2023

Description:
This script reads in a Markdown file, processes it, and converts it to a .docx file. 
The processing step involves finding footnote-style references and converting them into 
hyperlinks to a Google search query for the referenced text.

Limitations:
1. The hyperlinks will direct to a Google search result page, not the actual source. The 
   accuracy of the target depends on the search results.
2. The script uses Python's inbuilt urllib.parse to encode the text for the URLs. This 
   might not work perfectly with all characters in all languages.
3. The bullet point list formatting and the center alignment of the references are not 
   perfect due to the limitations of Markdown and pypandoc.
4. Due to the limitations of `pypandoc` and the complexity of translating Markdown to `.docx`, 
   it isn't possible to implement a footnote system where clicking on the superscript numbers 
   in the body of the text takes you to the references section.
"""

import os
import urllib.parse
from weasyprint import HTML

def convert_md_to_docx(input_file_path, output_file_path=None):
    """
    Converts a Markdown file to a .docx file, turning footnote-style references into hyperlinks 
    to Google search queries for the referenced text.

    Parameters:
    input_file_path (str): The path to the input .md file.
    output_file_path (str, optional): The path to save the output .docx file. 
    If not specified, it uses the same path and name as the input file, with the extension changed to .docx.
    """

    # If no output file path is provided, use the same name as the input file but with a .docx extension
    if output_file_path is None:
        file_name, _ = os.path.splitext(input_file_path)
        output_file_path = file_name + '.docx'

    # Read the Markdown content
    with open(input_file_path, 'r') as f:
        md_content = f.read()

    # Identify the reference section
    ref_start_index = md_content.find("**References**")
    references_content = md_content[ref_start_index:]
    md_content = md_content[:ref_start_index]

    # Check for references
    reference_pattern = re.compile(r'\[\^\d+\^\]:\s(.*)')
    references = reference_pattern.findall(references_content)

    # Start a new markdown list for the references and add some space before the reference section
    ref_list_md = "\n\n**References**\n\n"
    for i, reference in enumerate(references, start=1):
        # URL encode the reference to use in a Google search
        url_encoded_reference = urllib.parse.quote_plus(reference)
        google_search_url = f'https://www.google.com/search?q={url_encoded_reference}'
        # Create a markdown link to the Google search, and add it as a list item
        ref_list_md += f'- [{i}: {reference}]({google_search_url})\n\n'  # Added an extra newline character here

    # Add the new references list to the end of the content
    md_content += ref_list_md

    # Convert the Markdown content to HTML using pypandoc
    html_content = pypandoc.convert_text(md_content, 'html', format='md')

    # Save the HTML to a temporary file
    temp_html_file = "temp.html"
    with open(temp_html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Convert the HTML to DOCX using weasyprint
    HTML(temp_html_file).write_pdf(output_file_path, stylesheets=[CSS(string='@page { size: A4; margin: 1.5cm; }')])

    # Remove the temporary HTML file
    os.remove(temp_html_file)

# Example usage
convert_md_to_docx('/Users/davidvanderbyl/Documents/Home/Gardening/plants.md')  # This will produce 'yourfile.docx'
