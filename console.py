#!/usr/bin/python3

import cmd


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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
