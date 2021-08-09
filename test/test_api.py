"""
Created by Vivek Kumar on 7/27/21
"""
import unittest
from simplefilebrowser.api import app

TEST_PATH_VALID = "//test"
TEST_PATH_INVALID = "/Users/vivekk_28/Vi/code/playground/github/simple-file-browsers"
TEST_FILE_PATH = "/Users/vivekk_28/Vi/code/playground/github/simplefilebrowser/simplefilebrowser/exceptions.py"

class TestSFBAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = app.SimpleFileBrowserAPI()

    # def test_valid_root(self):
    #     path = TEST_PATH_VALID
    #     contents = TestFileBrowser.file_browser.show_dir(path)
    #     self.assertIsNotNone(contents)

    # def test_invalid_root(self):
    #     path = TEST_PATH_INVALID
    #     with self.assertRaises(FileExistsError):
    #         TestFileBrowser.file_browser.show_dir(path)

    # def test_show_file_contents(self):
    #     path = TEST_FILE_PATH
    #     contents = TestFileBrowser.file_browser.show_file(path)
    #     print(contents)
    #     assert len(contents) > 0

if __name__ == '__main__':
    unittest.main()
