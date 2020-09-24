import unittest
import search_root_with_tree_class
from search_root_with_tree_class import main as get_root

TESTDATA_FILENAME = 'input_file.txt'
TESTDATA_FILENAME2 = 'input_empty.txt'
TESTDATA_FILENAME3 = 'input_unbalanced.txt'
#TESTDATA_FILENAME4 = 'input_repeating.txt'
#TESTDATA_FILENAME5 = 'input_node_only.txt'
#TESTDATA_FILENAME6 = 'input_invalid_chars.txt'
#TESTDATA_FILENAME6 = 'input_large_tree.txt'


class TreeTests(unittest.TestCase):
    """Tests for `search_root_with_tree_class.py`."""
    
    def test_question_cases(self):
        self.assertEqual(get_root(TESTDATA_FILENAME), 2)

    def test_empty_file(self):
        with self.assertRaises(Exception): get_root(TESTDATA_FILENAME2)

    def test_unbalanced_tree(self):
        self.assertEqual(get_root(TESTDATA_FILENAME3), 1)
    """
    def test_repeating_labels(self):
        with assertRaises(Exception): get_root(TESTDATA_FILENAME4)
    
    def test_no_children(self):
        self.assertEqual(get_root(TESTDATA_FILENAME5), 2)

    def test_invalid_characters(self):
        self.assertEqual(get_root(TESTDATA_FILENAME6), 2)
    
    def test_large_tree(self):
        self.assertEqual(get_root(TESTDATA_FILENAME7), 2)
        
        """
  

if __name__ == '__main__':
    unittest.main()