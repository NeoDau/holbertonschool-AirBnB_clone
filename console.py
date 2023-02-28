#!/usr/bin/python3
"""shebang"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for console airbnb"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

    def do_EOF(self, arg):
        """eof cmd function"""
        return True

    def do_quit(self, arg):
        """quit cmd"""
        return True

    def help_quit(self, arg):
        """quit"""
        print("quit")

    def help_EOF(self, arg):
        """eof"""
        print("EOF")

    def emptyline(self):
        pass

    def do_create(self, args):
        """ Creates a new instance """
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.classes[arg[0]]()
            print(instance.id)
            instance.save()
 
    def do_show(self, args):
        """ Prints str representation of an instance """
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            try:
                eval(arg[0])
                try:
                    sto = atroage.all()
                    print(sto[f"{string_split[0]}.{string_split[1]}"])
                except Exception:
                    print("** nos instance found **")
            except Exception:
                print("** class doesn't exist")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            try:
                eval(arg[0])
                try:
                    del storage.all()[f"{arg[0]}.{arg[1]}"]
                    storage.save()
                except Exception:
                    print("** no instance fund **")
            except Exception:
                print("** class dosen't exist")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        arg = args.split()
        if len(args) >= 1:
            try:
                eval(args)()
                print(storage.all())
            except Exception:
                print('** class doesn\'t exist **')
        else:
            print(storage.all())

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in classes:
            if len(arg) > 1:
                key = arg[0] + '.' + arg[1]
                if key in storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            setattr(storage.all()[key], arg[2], arg[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
