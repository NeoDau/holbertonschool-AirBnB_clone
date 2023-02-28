#!/usr/bin/python3
"""shebang"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

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
        args = arg.split()
        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = eval[args]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """priont str representation of a instance"""
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            try:
                eval(arg[0])
                try:
                    sto = storage.all()
                    print(sto[f"{strSplit[0]}.{strSplit[1]}"])
                except Exception:
                    print("** no istance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """del instance based the class"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) < 2:
            print("** instance id missing **")
        if arg[0] not in classes:
            print("** class dosen't exist **")
            return
        for key, value in storage.all().items():
            if arg[1] == value.id:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance fund **")

    def do_all(self, arg):
        """print atr reptesentation all instance"""
        args = arg.split()

        if not args:
            print(list((storage.all())))
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            list_all = []
            storage.reload()
            for obj_id in storage.all().keys():
                if obj_id.split(".")[0] == inputs[0]:
                    list_all.append(str(storage.all()[obj_id]))
            print(list_all)

    def do_update(self, arg):
        """update a istance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
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
if __name__ == "__main__":
    HBNBCommand().cmdloop()
