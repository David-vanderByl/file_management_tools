# This is a title

This is a paragraph.

## This is a subheading

This is another paragraph.

```python
# This is some Python code
print('Hello, world!')
print('second line')
```

This is yet another paragraph.

```
This is a code block without a specified language.
```

This is a final paragraph.



Here's a unit test for the script:

```python
import unittest
import json
import os

# You should have the function `md_to_ipynb` defined here or imported from another file.

class TestMdToIpynb(unittest.TestCase):

    def test_md_to_ipynb(self):
        # Convert the test.md file to a notebook
        md_to_ipynb('test.md')
        
        # Check that the notebook file was created
        self.assertTrue(os.path.isfile('test.ipynb'))

        # Load the notebook
        with open('test.ipynb', 'r') as f:
            notebook = json.load(f)
        
        # Check the notebook structure
        self.assertIn('cells', notebook)
        self.assertIsInstance(notebook['cells'], list)
        
        # Check the cells
        self.assertEqual(len(notebook['cells']), 7)
        self.assertEqual(notebook['cells'][0]['cell_type'], 'markdown')
        self.assertEqual(notebook['cells'][0]['source'], '# This is a title\n')
        self.assertEqual(notebook['cells'][2]['cell_type'], 'markdown')
        self.assertEqual(notebook['cells'][2]['source'], '## This is a subheading\n')
        self.assertEqual(notebook['cells'][4]['cell_type'], 'code')
        self.assertEqual(notebook['cells'][4]['source'], '# This is some Python code\nprint(\'Hello, world!\')\n')
        self.assertEqual(notebook['cells'][6]['cell_type'], 'code')
        self.assertEqual(notebook['cells'][6]['source'], 'This is a code block without a specified language.\n')

if __name__ == '__main__':
    unittest.main()
```