#!/usr/bin/python3
"""
Module for TestHBNBCommand class
"""
import unittest
import console
from console import HBNBCommand
import os
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO


class Test_console(unittest.TestCase):
    """
    Tests HBNBCommand console
    """

    def setUp(self):
        """
        Sets up test cases
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.reset_storage()

    def tearDown(self):
        """
        Tears down test cases
        """
        self.reset_storage()

    def reset_storage(self):
        """
        Resets FileStorage data
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_do_EOF(self):
        """
        Test for the method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

    def test_do_quit(self):
        """
        Tests quit commmand
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def create(self):
        """
        create the intance
        """
        return HBNBCommand()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
