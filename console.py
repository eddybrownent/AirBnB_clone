#!/usr/bin/python3
"""
This script contains the entry point of command interpreter
"""

import cmd

from models.base_model import BaseModel
from models import storage
<<<<<<< HEAD

=======
>>>>>>> 1c77a714ceae08d82366fe229a0f7d3ebe65dbef
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class for the command line interpreter
    """
    prompt = "(hbnb) "
<<<<<<< HEAD
    __classes = {"BaseM", "Usr", "St", "City", "Amenity", "Place", "Review"}
=======
    __classes = {"BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"}
>>>>>>> 1c77a714ceae08d82366fe229a0f7d3ebe65dbef

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
            storage.save()

    def do_show(self, arg):
        """
        Prints representation of an instance based on class name and id
        """
        args = arg.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()

        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            all_instances = []
            instances = storage.all().values()
            for instance in instances:
                if len(args) > 0 and args[0] == instance.__class.__name__:
                    all_instances.append(str(instance))
                elif len(args) == 0:
                    all_instances.append(str(instance))
            print(all_instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        adding or updating attribute
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]

            if class_name not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                instances = storage.all()

                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key not in instances:
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    attr_value = attr_value.replace('"', "")
                    instance = instances[instance_key]

                    if hasattr(instance, attr_name):
                        setattr(instance, attr_name, attr_value)
                    else:
                        setattr(instance, attr_name, attr_value)
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
