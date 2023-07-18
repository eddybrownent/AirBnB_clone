#!/usr/bin/python3
"""
Custom Test Cases for FileStorage Class
"""
import unittest
from models.engine.file_storage import FileStorage


class CustomFileStorageTest(unittest.TestCase):
    """
    Custom Test Cases for FileStorage Class
    """

    def test_filestorage_instantiation(self):
        """
        Test FileStorage instantiation
        """
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_filestorage_methods_existence(self):
        """
        Test the existence of FileStorage methods
        """
        file_storage = FileStorage()
        self.assertTrue(hasattr(file_storage, 'all'))
        self.assertTrue(hasattr(file_storage, 'new'))
        self.assertTrue(hasattr(file_storage, 'save'))
        self.assertTrue(hasattr(file_storage, 'reload'))

if __name__ == '__main__':
    unittest.main()

