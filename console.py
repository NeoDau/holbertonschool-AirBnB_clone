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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
