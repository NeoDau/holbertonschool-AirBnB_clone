#!/usr/bin/python3
"""shebang"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class for console airbnb"""
    prompt = "(hbnb) "

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

    def de_create(self, arg):
        """create instance"""
        if not (arg):
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = eval[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """priont str representation of a instance"""
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            try:
                eval(arg[0])
                try:
                    sto = storage.all()
                    print(sto[f"{strSplit[0]}.{strSplit[1]}"])
                except Exception:
                    print("** no istance fund **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """del instance based the class"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) < 2:
            print("** instance id missing **")
        for key, value in storage.all().items():
            if arg[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance fund **")

    def do_all(self, arg):
        """print atr reptesentation all instance"""
        arg = arg.split()
        if len(arg) >= 1:
            try:
                eval(arg)()
                print(storage.all())
            except Exception:
                print("** class doesn\'t exist **")
        else:
            print(storage.all())

    def do_update(self, arg):
        """update a istance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            try:
                eval(args[0])
                try:
                    for key, value in storage.all().items():
                        obj = value
                        if key == f"{string_split[0]}.{string_split[1]}":
                            setattr(obj, args[2], args[3])
                except Exception:
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
