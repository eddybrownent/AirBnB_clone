#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb) '

	def do_quit(self, arg):
		"""Exit the program"""
		return True
    
	def do_EOF(self, arg):
		"""Exit the program"""
		return True

		
	def do_help(self, arg):
		"""List available commands"""
		cmd.Cmd.do_help(self, arg)

	def emptyline(self):
		pass
	def do_create(self, arg):
		"""create a new class instance and print"""
		if len(arg) == 0:
			print("** class name missing **")
		elif arg[0] not in HBNBCommand:
			print("** class doesn't exist **")
		else:
			print(arg[0]().id)
			
if __name__ == '__main__':
    HBNBCommand().cmdloop()
