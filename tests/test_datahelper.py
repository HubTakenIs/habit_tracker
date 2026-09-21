import unittest
from datahelper import setup_data_folder
import os

class setup_tests(unittest.TestCase):
    @unittest.skip("Testing skip")
    def test_setup_data_folder(self):
       abs_path = os.path.abspath("./data/")
       before_setup = os.path.exists(abs_path)
       self.assertFalse(before_setup)
       setup_data_folder()
       after_setup = os.path.exists(abs_path) and os.path.isdir(abs_path)
       self.assertTrue(after_setup)

