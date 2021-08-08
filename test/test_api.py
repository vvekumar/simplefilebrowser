"""
Created by Vivek Kumar on 7/27/21
"""
import unittest
from simplefilebrowser.browser import filebrowser as fb

TEST_PATH_VALID = "//test"
TEST_PATH_INVALID = "/Users/vivekk_28/Vi/code/playground/github/simple-file-browsers"
TEST_FILE_PATH = "/Users/vivekk_28/Vi/code/playground/github/simplefilebrowser/simplefilebrowser/exceptions.py"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
