#!/usr/bin/env python3
"""
Unittests for AgriMarket console
"""

import sys
sys.path.append('/home/AgriMarket')
import unittest
from unittest.mock import patch
from io import StringIO
from console import AMCommand


class TestAMCommand(unittest.TestCase):
    def setUp(self):
        self.console = AMCommand()


    def tearDown(self):
        pass


    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue(), "")


    def test_create_user(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())


    def test_show_user(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show User 1234"))
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    
    def test_create_product(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Product"))
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())


    def test_show_product(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show Product 1234"))
            self.assertIn("** no instance found **", mock_stdout.getvalue())


    def test_create_equipment(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Equipment"))
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    def test_show_equipment(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show Equipment 1234"))
            self.assertIn("** no instance found **", mock_stdout.getvalue())


    # Add more test cases for other commands like destroy, update, and more

if __name__ == "__main__":
    unittest.main()
