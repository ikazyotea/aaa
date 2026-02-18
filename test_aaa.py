#!/usr/bin/env python3
"""
Tests for aaa.py
"""
import unittest
from io import StringIO
import sys
from aaa import main


class TestAaa(unittest.TestCase):
    """Test cases for aaa module"""
    
    def test_main_output(self):
        """Test that main() prints 'aaa'"""
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            main()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "aaa")


if __name__ == "__main__":
    unittest.main()
