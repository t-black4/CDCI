# Test File
import unittest
import sys
import os

# Ensure the src directory is included in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import main

class TestMain(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
