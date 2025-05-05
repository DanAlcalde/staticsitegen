import unittest

from generate import extract_title


class TestGenerate(unittest.TestCase):
    def test_extract(self):
        title = extract_title("# This is a title")
        self.assertEqual(title, "This is a title")

    def test_extract_no_title(self):
        with self.assertRaises(Exception):
            extract_title("This is not a title")
    
    



if __name__ == "__main__":
    unittest.main()