"""
Custom Requirements Generator

This script generates a requirements.txt file containing external module imports
from a Python project directory. It analyzes the Python files in the project and
identifies the external modules that are used. It excludes locally installed packages
and their top-level modules from the list of imports.

Usage:
    python custom_requirements_generator.py

Note:
    - Modify the 'project_root' variable to point to the root directory of your project.
    - The generated 'requirements.txt' file will be saved in the project root directory.

Author: David van der Byl
Date: -/-/2023
"""


import os
import ast
import sys

def get_all_imports(root_directory):
    """
    Extracts all import statements from Python files within the specified root directory.

    Args:
        root_directory (str): The root directory to search for Python files.

    Returns:
        list: List of unique import module names.
    """
    
    imports = set()
    for root, _, files in os.walk(root_directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as f:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for subnode in node.names:
                                imports.add(subnode.name)
                        elif isinstance(node, ast.ImportFrom):
                            imports.add(node.module)
    return list(imports)




def get_locally_installed_packages():
    """
    Retrieves locally installed packages along with their top-level modules.

    Returns:
        list: List of dictionaries containing package names and associated top-level modules.
    """
    
    packages = []
    for path in sys.path:
        if 'site-packages' in path:
            package_name = os.path.basename(path)
            top_level_modules = [f.split('.')[0] for f in os.listdir(path) if f.endswith('.py')]
            packages.append({'name': package_name, 'top_level_modules': top_level_modules})
    return packages


def filter_external_imports(all_imports, locally_installed_packages):
    """
    Filters out locally installed packages and their top-level modules from the list of all imports.

    Args:
        all_imports (list): List of all import module names.
        locally_installed_packages (list): List of dictionaries containing locally installed package names and top-level modules.

    Returns:
        list: List of external import module names.
    """
    
    external_imports = []
    for imp in all_imports:
        for pkg in locally_installed_packages:
            if imp in pkg['top_level_modules']:
                break
        else:
            external_imports.append(imp)
    return external_imports



def generate_requirements_txt(root_directory):
    
    """
    Generates a requirements.txt file containing external module imports.

    Args:
        root_directory (str): The root directory of the project.

    Writes:
        A requirements.txt file in the project root directory.
    """
    
    all_imports = get_all_imports(root_directory)
    locally_installed_packages = get_locally_installed_packages()
    external_imports = filter_external_imports(all_imports, locally_installed_packages)

    with open(os.path.join(root_directory, 'requirements.txt'), 'w') as f:
        f.write('\n'.join(external_imports))


if __name__ == '__main__':
    project_root = '/Users/davidvanderbyl/Documents/GitHub/file_management_tools'
    generate_requirements_txt(project_root)
