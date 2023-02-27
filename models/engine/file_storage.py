#!/usr/bin/python3
"""shebang"""
import json


class FileStorage:
    """file saver class"""

    __file_path = "save.json"
    __objects = {}

    def all(self):
        """return dict of obj"""
        return self.__objects

    def new(self, obj):
        """set data in dict attribute"""
        x = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[x] = obj

    def save(self):
        """save obj in file json str"""
        dictCopy = {}

        for x in self.__objects:
            dictCopy[x] = self.__objects[x].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dictCopy, f)

    def reload(self):
        """reload model the of from path"""
        try:
            with open(self.__file_path) as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(value["__clas__"])(**value)
        except Exception:
            pass
