#!/usr/bin/python3
""" """
from tests.test_base_model import test_basemodel
from models.user import user

class test_User(test_basemodel):
"""unittest for testing instantiation of the user class"""

	def __init__(self, *args, **kwargs):
	""" """
	super().__init__(*args, **kwargs)
	self.name = "User"
	self.value = User

	def test_first_name(self):
	""" """
	new = self.value()
	self.assertEqual(type(new.first_name), str)

	def test_last_name(self):

	new = self.value()
	self.assertEqual(type(new.last_name), str)

	def test_email(self):
	'''tests the email'''
	new = self.value()
	self.assertEqual(type(new.email), str)

	def test_password(self):
	'''tests the password'''
	new = self.value()
	self.assertEqual(type(new.password), str)
