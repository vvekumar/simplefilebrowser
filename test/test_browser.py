"""
Created by Vivek Kumar on 7/27/21
"""
import os
import unittest
from simplefilebrowser.browser import filebrowser as fb

TEST_PATH_VALID = os.path.dirname(os.path.realpath(__file__))
TEST_PATH_INVALID = "/does/not/exist"
TEST_FILE_PATH = os.path.realpath(__file__)

class TestFileBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_browser = fb.SimpleFileBrowser()

    def test_valid_root(self):
        path = TEST_PATH_VALID
        contents = TestFileBrowser.file_browser.show_dir(path)
        self.assertIsNotNone(contents)

    def test_invalid_root(self):
        path = TEST_PATH_INVALID
        with self.assertRaises(FileNotFoundError):
            TestFileBrowser.file_browser.show_dir(path)

    def test_show_file_contents(self):
        path = TEST_FILE_PATH
        contents = TestFileBrowser.file_browser.show_file(path)
        print(contents)
        assert len(contents) > 0

if __name__ == '__main__':
    unittest.main()
