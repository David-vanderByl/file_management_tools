import re
import os

def read_file_content(file_path):
    """Open and read the contents of the provided file."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_code(content, languages):
    """
    Use a regular expression to find the code blocks and associated file names.
    The pattern first tries to find a file name followed by a code block.
    It then captures the content between these code blocks, excluding the language specification.
    """
    # Regular expression pattern
    pattern = r"(\w+\.(?:{}))\s*```(?:{}).*?\n((?:.|\n)*?)\s*```".format("|".join(languages), "|".join(languages))
    file_pairs = re.findall(pattern, content, re.DOTALL)

    # Iterate over each file pair and remove leading/trailing whitespaces from the code
    file_pairs = [(name, code.strip()) for name, code in file_pairs]

    return file_pairs

def write_files_from_chat(file_pairs, output_dir):
    """
    Write each parsed code block to a separate file in the output directory.
    """
    for file_pair in file_pairs:
        file_name, code_block = file_pair
        complete_file_name = "".join(file_name)  # Join elements of tuple to form complete file name
        file_path = os.path.join(output_dir, complete_file_name)
        with open(file_path, 'w') as f:
            f.write(code_block)

if __name__ == "__main__":
    # Define the path to the input text file
    file_path = 'DS_toolbox/box_1_data_collection/web_extraction_tools/allcode.txt'

    # Define the directory where the output code files should be saved
    output_dir = 'test'

    # List of programming languages the script should recognize
    languages = ["py", "js"]

    # Read the content of the input text file
    content = read_file_content(file_path)

    # Parse the content to extract the code blocks and associated file names
    file_pairs = parse_code(content, languages)

    # Write each code block to a separate file in the output directory
    write_files_from_chat(file_pairs, output_dir)
