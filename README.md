# File Management Tools

Welcome to the **File Management Tools** repository! This collection of tools aims to simplify various file management tasks, making your development workflow more efficient. The tools provided in this repository cover tasks like generating requirements files, creating project structures, converting file formats, and more.

## Table of Contents

- [Tools](#tools)
- [Installation](#installation)
  - [Using pip and virtual environment](#using-pip-and-virtual-environment)
  - [Using conda environment](#using-conda-environment)
- [Usage](#usage)
- [Testing](#testing)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Tools

- [generate_requirements_txt.py](tools/generate_requirements_txt.py)
- [notebook_TOC.py](tools/notebook_TOC.py)
- [ipynb_to_md.py](tools/ipynb_to_md.py)
- [file_struct.py](tools/file_struct.py)
- [txt_to_code.py](tools/txt_to_code.py)
- [project_struct_create.py](tools/project_struct_create.py)
- [initi_generator.py](tools/initi_generator.py)
- [md_to_word.py](tools/md_to_word.py)
- [md_to_ipynb.py](tools/md_to_ipynb.py)
- [code_to_txt.py](tools/code_to_txt.py)

## Installation

You can install the required dependencies using `pip` or `conda` environments. It's recommended to set up a virtual environment before installing the dependencies.

### Using pip and virtual environment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/file_management_tools.git
   cd file_management_tools
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Using conda environment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/file_management_tools.git
   cd file_management_tools
   ```

2. Create a new conda environment:

   ```bash
   conda create --name file-tools-env python=3.9
   conda activate file-tools-env
   ```

3. Install the dependencies from `requirements.txt` using pip within the conda environment:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once you have the required dependencies installed, you can use the tools by running their respective scripts. Each tool has its own functionality, and you can find more information about their usage by checking the source code or the documentation.

## Testing

Unit tests are provided to ensure the functionality of the tools. You can run the tests using a testing framework such as `pytest`.

To run the tests:

1. Install `pytest` (if not already installed):

   ```bash
   pip install pytest
   ```

2. Navigate to the `tests` directory:

   ```bash
   cd tests
   ```

3. Run the tests:

   ```bash
   pytest
   ```

## File Structure

The repository's file structure is organized as follows:

- `tools/`: Directory containing the tools' source code.
- `tests/`: Directory containing unit tests for the tools.
- `requirements.txt`: List of required Python packages.
- `file_management_tools.code-workspace`: Visual Studio Code workspace settings.
- `README.md`: This README file.
- `.gitignore`: List of files and directories to be ignored by Git.
- `file_structure.txt`: A sample file structure description.

## Contributing

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.