#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {"BaseModel"}

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
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
			
if __name__ == '__main__':
    HBNBCommand().cmdloop()
