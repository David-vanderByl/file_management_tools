import os
import sys

# Get the path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path of the root directory
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..'))

# Add the root directory to the system path
sys.path.append(root_dir)


from DS_toolbox.utils.file_management.initi_generator import get_symbols_to_include, create_init_file

def test_get_symbols_to_include():
    # Use a script file you know the result for as test input
    symbols = get_symbols_to_include('path_to_your_script.py')
    assert isinstance(symbols, list)
    # Assert the known result
    assert symbols == ['your_known_symbols']

def test_create_init_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.py"
    p.write_text("def hello():\n    return 'Hello World!'\n")

    create_init_file(str(d))

    assert (d / "__init__.py").exists()