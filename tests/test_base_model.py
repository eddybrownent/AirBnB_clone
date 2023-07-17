#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
import json
import os
import models


class test_basemodel(unittest.TestCase):
	""" """
	def __init__(self, args, **kwargs):
	""" """
	super().__init__(*args, **kwargs)
	self.name = 'BaseModel'
	self.value = BaseModel
	
	def setUp(self):
	""" """
		pass
	
	def test_id(self):
	""" """
	new = self.value()
	self.assertEqual(type(new.id), str)

	def test_create_at(self):
	""" """
	new = self.value()
	self.assertEqual(type(new.created_at), datetime.datetime)
	
	def test_updated_at(self):
	""" """
	new = self.value()
	self.assertEqual(type(new.updated_at), datetime.datetime)
	k = new.to_dict()
	new = BaseModel(**k)
	self.asserFalse(new.created_at == new.updated_at)
