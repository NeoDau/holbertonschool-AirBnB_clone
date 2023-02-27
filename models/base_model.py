#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """class create"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        #[<class name>] (<self.id>) <self.__dict__>
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        newDict = self.__dict__.copy()
        newDict["__class__"] = self.__class__.__name__
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.updated_at.isoformat()
        return newDict

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
