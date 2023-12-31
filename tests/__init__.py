#!/usr/bin/python3
"""
This script initializes the FileStorage object
and reloads the stored data
"""

from models.engine.file_storage import FileStorage


"""A variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
