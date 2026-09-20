import unittest
from datahelper import DataHelper
import os

class setup_tests(unittest.TestCase):
    
    def test_setup_data_folder(self):
       datahelper = DataHelper()
       abs_path = os.path.abspath("./data/")
       before_setup = os.path.exists(abs_path)
       self.assertFalse(before_setup)
       datahelper.setup_data_folder()
       after_setup = os.path.exists(abs_path) and os.path.isdir(abs_path)
       self.assertTrue(after_setup)

