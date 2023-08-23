import os


def create_file_structure_file(root_dir):
    """
    Creates a file structure representation of the project directory and saves it in a file named file_structure.txt.

    Args:
        root_dir (str): The project root directory.

    Returns:
        None
    """
    output_file = "file_structure.txt"
    with open(output_file, 'w') as file:
        p = f"{root_dir}\n"
        print(p)
        file.write(f"{root_dir}\n")  # Write the project root directory
        file.write(generate_file_structure(root_dir))  # Generate and write the file structure


def generate_file_structure(directory, indent=""):
    """
    Generates a file structure representation for the given directory.

    Args:
        directory (str): The directory to generate the file structure representation for.
        indent (str): The current indentation level.

    Returns:
        str: The file structure representation.
    """
    file_structure = ""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item == "__pycache__":
            continue  # Skip __pycache__ directory
        if os.path.isfile(item_path):
            file_structure += f"{indent}├─ {item}\n"  # Add file representation
        elif os.path.isdir(item_path):
            file_structure += f"{indent}├─ {item}/\n"  # Add directory representation
            file_structure += generate_file_structure(item_path, indent + "│  ")  # Recursive call for subdirectories
    return file_structure



if __name__ == "__main__":
    # project_root = input("Enter the project root directory: ")
    project_root = '/Users/davidvanderbyl/Documents/GitHub/file_management_tools'
    output_file= project_root
    create_file_structure_file(project_root)
    print("File structure created successfully!")
