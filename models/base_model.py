#!/usr/bin/python3
"""defining basemodel class"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Class Base defines all common attributes or methods for other classes
    Attr:
    id: string - assign with a uuid when an instance is created
    created_at: datetime - assign with the current datetime 
    when an instance is created
    updated_at: datetime - assign with the current datetime 
    when an instance is created and it will be updated 
    every time you change your object

    """
    def __init__(self, *args, **kwargs):
        """
        new BaseModel
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], 
							form)
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], form)
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        """
        returns a dictionary containing all
         keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """Representation of BaseModel instance"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
