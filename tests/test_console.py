#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import pycodestyle
import unittest
from io import StringIO
from unittest.mock import patch
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_create_command(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length

    def test_invalid_command(self):
        """Test an invalid command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: invalid_command")


if __name__ == '__main__':
    unittest.main()
