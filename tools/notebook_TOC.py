import nbformat
import re
from slugify import slugify

# still a work in process ONLY RUN ONCE at when you have finished making sections in your ipynb

def create_and_insert_toc(ipynb_file, highest_heading_level):
    nb = nbformat.read(ipynb_file, as_version=4)

    # Regular expression pattern to find header lines in markdown cell
    pattern = r"^(#+)\s*(\d+\.)*\s*(.*)$"

    # Keep track of current section numbers
    section_numbers = [0] * highest_heading_level
    headers = []
    toc_index = 0
    section_start = False

    # Loop through each cell in the notebook
    for i, cell in enumerate(nb.cells):
        # If the cell is a markdown cell
        if cell.cell_type == "markdown":
            # Check if TOC already exists
            if cell.source.startswith("# Table of Contents"):
                nb.cells.pop(i)  # Delete existing TOC
                continue

            # Find all the headers in the cell's source
            matches = re.finditer(pattern, cell.source, re.MULTILINE)
            
            for match in matches:
                level = len(match.group(1))
                heading = match.group(3).lstrip("0123456789. ")  # Remove old numbering if it exists
                
                if level < highest_heading_level:
                    # This is not a section header, ignore it
                    continue
                elif level == highest_heading_level:
                    # We've reached the first section, start counting sections
                    section_start = True

                if not section_start:
                    # We're still in the title area, move the TOC index to the next cell
                    toc_index += 1
                    continue

                if level > len(section_numbers):
                    # This level hasn't been encountered yet, extend the list
                    section_numbers.extend([0] * (level - len(section_numbers)))

                # Increase the section number and reset all subsection numbers
                section_numbers[level - 1] += 1
                section_numbers[level:] = [0] * len(section_numbers[level:])

                # Generate the new section number
                section_number = ".".join(str(n) for n in section_numbers[:level] if n > 0)

                # Generate the new header line with section number and hyperlink
                new_header = match.group(1) + " " + section_number + " " + heading

                # Replace the original header line with the new one
                cell.source = re.sub(pattern, new_header, cell.source, flags=re.MULTILINE)

                # Add the new header to the list of headers
                headers.append((level - highest_heading_level, section_number + " " + heading))

    # Create the TOC
    toc = ["# Table of Contents"]
    for level, heading in headers:
        toc.append("  " * level + "- [" + heading + "](#" + slugify(heading) + ")")

    # Create a new markdown cell for the TOC
    toc_cell = nbformat.v4.new_markdown_cell(source="\n".join(toc))

    # Insert the TOC cell
    nb.cells.insert(toc_index, toc_cell)

    # Write the new notebook to file
    nbformat.write(nb, ipynb_file)

# To test, call create_and_insert_toc("your_file.ipynb", 2)


# To test, 
if __name__ == "__main__":
    file_path = "/Users/davidvanderbyl/Documents/GitHub/Data_Science_Handbooks/temp/pandas.ipynb"
    create_and_insert_toc(ipynb_file=file_path, highest_heading_level=2)
