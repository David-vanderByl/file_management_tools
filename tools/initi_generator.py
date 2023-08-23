"""
Auto-generate or update __init__.py

This script automatically generates or updates the __init__.py file in a given directory
to include function and class names from Python scripts. It provides an option to update
or replace the __init__.py file based on user input.

Usage:
1. Replace 'file_path' with the target directory path.
2. Run the script.

Limitations:

- When replace = False the __init__.py file is updated during which the file is 
only added to so if you deleted functions/classes in a given script they will remain
in the __init__.py file.

- If a function or class is called by another besides `if __name__ == "__main__":` 
those will not be included in the __init__.py, so you'll have to add these 
manually then make sure to only use replace = False so they not deleted when updating 
the generated file.

Author: David
Date: -/-/23
"""

import os
import ast

def get_symbols_to_include(file_path):
    """
    Extracts symbols (i.e., function and class names) to be included in __init__.py file 
    from a Python script.

    Parameters:
    file_path (str): The path to the Python script.

    Returns:
    List[str]: A list of strings containing function and class names to be included.
    """
    
    # Open the Python script and read its content.
    with open(file_path) as f:
        file_content = f.read()

    # Parse the Python script into an abstract syntax tree (AST).
    module = ast.parse(file_content)

    # Get top-level class names defined in the script, excluding '__init__' and nested classes.
    top_level_class_names = [node.name for node in module.body
                             if isinstance(node, ast.ClassDef) and
                             node.name != '__init__' and node.col_offset == 0
                             ]

    # Get top-level function names defined in the script, excluding '__init__' and nested functions.
    top_level_function_names = [node.name for node in module.body
                                if isinstance(node, ast.FunctionDef) and 
                                node.name != '__init__' and node.col_offset == 0
                                ]

    # Get the names of all function calls made in the script.
    all_calls = [node.func.id for node in ast.walk(module) 
                 if isinstance(node, ast.Call) and 
                 isinstance(node.func, ast.Name)
                 ]

    # Check if a function named "main" is defined in the script.
    main_func = next((node for node in module.body 
                      if isinstance(node, ast.FunctionDef) and 
                      node.name == 'main'), None)
    
    # If a "main" function is defined, get the names of all function calls made within it.
    main_calls = [node.func.id for node in ast.walk(main_func) 
                  if isinstance(node, ast.Call) and 
                  isinstance(node.func, ast.Name)
                  ] if main_func else []

    # Check if an "if __name__ == '__main__'" block is present in the script.
    main_block = next((node for node in module.body 
                       if isinstance(node, ast.If) and 
                       isinstance(node.test, ast.Compare) and 
                       isinstance(node.test.left, ast.Name) and 
                       node.test.left.id == '__name__'), None
                      )
    
    # If an "if __name__ == '__main__'" block is present, get the names of all function calls made within it.
    main_block_calls = [node.func.id for node in ast.walk(main_block) 
                        if isinstance(node, ast.Call) and 
                        isinstance(node.func, ast.Name)
                        ] if main_block else []

    # Include top-level functions if they're not called anywhere in the script 
    # or are called within the "main" function or the "if __name__ == '__main__'" block.
    functions_to_include = [fn for fn in top_level_function_names 
                            if fn not in all_calls or 
                            fn in main_calls or 
                            fn in main_block_calls
                            ]

    # Return the class names and function names to be included in the "__init__.py" file.
    return top_level_class_names + functions_to_include



def create_init_file(directory, replace=False):
    """
    Creates or updates an __init__.py file in a given directory.

    Parameters:
    directory (str): The path to the directory where the __init__.py file should be created.
    replace (bool, optional): If True, replace the existing __init__.py file. If False,
                             update the existing __init__.py file without deleting its content.

    Returns:
    None
    """
    
    if not os.path.exists(directory):
        print(f"Directory: {directory} does not exist.")
        return

    py_files = [f for f in os.listdir(directory) if f.endswith('.py')]
    init_file = os.path.join(directory, '__init__.py')
    
    existing_symbols = set()
    existing_init_content = ""

    if os.path.exists(init_file) and not replace:
        with open(init_file, 'r') as f:
            existing_init_content = f.read()
            existing_symbols = set([
                symbol.strip() for line in existing_init_content.split("\n") if line.strip() and line.startswith("from") and "import" in line
                for symbol in line.split("import")[1].split(",") if len(line.split("import")) > 1
            ])

    with open(init_file, 'w') as f:
        if existing_init_content:
            f.write(existing_init_content)
            f.write("\n\n")
        else:
            f.write("# This file makes the directory a Python package\n\n")

        all_symbols = []

        for py_file in py_files:
            symbols = get_symbols_to_include(os.path.join(directory, py_file))
            
            if symbols:
                base_name = py_file[:-3]
                for symbol in symbols:
                    if replace or symbol not in existing_symbols:
                        f.write(f"from .{base_name} import {symbol}\n")
                        all_symbols.append(f'"{symbol}"')

        if all_symbols:
            f.write("\n__all__ = [\n")
            f.write(',\n'.join(all_symbols))
            f.write("\n]\n")

    print(f"__init__.py file has been {'created' if replace else 'updated'} in {directory}.")




def main(file_path, replace):
    create_init_file(file_path, replace)


if __name__ == "__main__":
    # The path to the directory where the "__init__.py" file should be created or updated.
    directory_path = "/Users/davidvanderbyl/Documents/GitHub/file_management_tools/tools"
    main(directory_path, replace=False)
