import os


def create_project_structure(root_dir):
    dirs = [
        'data',
        'notebooks',
        'src',
        'models',
        'reports',
        'tests',
    ]

    sub_dirs = [
        os.path.join('data', 'raw'),
        os.path.join('data', 'processed'),
        os.path.join('data', 'external'),
        os.path.join('notebooks', 'exploratory'),
        os.path.join('notebooks', 'prototyping'),
        os.path.join('src', 'data'),
        os.path.join('src', 'features'),
        os.path.join('src', 'models'),
        os.path.join('src', 'evaluation'),
        os.path.join('reports', 'figures'),
        os.path.join('reports', 'logs'),
        os.path.join('tests', 'unit'),
        os.path.join('tests', 'integration'),
    ]

    files = [
        os.path.join('src', '__init__.py'),
        os.path.join('src', 'data', '__init__.py'),
        os.path.join('src', 'features', '__init__.py'),
        os.path.join('src', 'models', '__init__.py'),
        os.path.join('src', 'evaluation', '__init__.py'),
        os.path.join('tests', '__init__.py'),
        os.path.join('tests', 'unit', '__init__.py'),
        os.path.join('tests', 'integration', '__init__.py'),
    ]

    for dir_path in dirs:
        os.makedirs(os.path.join(root_dir, dir_path))

    for sub_dir_path in sub_dirs:
        os.makedirs(os.path.join(root_dir, sub_dir_path))

    for file_path in files:
        with open(os.path.join(root_dir, file_path), 'w') as file:
            pass  # create an empty file






def create_project_structure(root_dir):
    dirs = [
        'src',
        'tests',
        'docs',
        os.path.join('src', 'controllers'),
        os.path.join('src', 'models'),
        os.path.join('tests', 'unit'),
        os.path.join('tests', 'integration'),
    ]

    files = [
        os.path.join('src', '__init__.py'),
        os.path.join('tests', '__init__.py'),
        os.path.join('tests', 'unit', '__init__.py'),
        os.path.join('tests', 'integration', '__init__.py'),
    ]

    for dir_path in dirs:
        os.makedirs(os.path.join(root_dir, dir_path))

    for file_path in files:
        with open(os.path.join(root_dir, file_path), 'w') as file:
            pass  # create an empty file


if __name__ == '__main__':
    project_root = input("Enter the project root directory: ")
    create_project_structure(project_root)
    print("Project structure created successfully!")
    # project_root = input("Enter the project root directory: ")
    project_root = '/Users/davidvanderbyl/Documents/CODE/PROJECTS/LLM_agent/src'
    create_project_structure(project_root)
    print("Project structure created successfully!")