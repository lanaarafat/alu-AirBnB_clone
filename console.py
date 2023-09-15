#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handle end of file"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def default(self, line):
        """Default behavior for unknown commands"""
        parts = line.split(".")
        if len(parts) != 2:
            print("*** Unknown syntax: {}".format(line))
            return
        class_name, method = parts
        if class_name not in self.classes:
            print("*** Unknown class: {}".format(class_name))
            return

        if method == "all()":
            self.do_all(class_name)
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_create(self, line):
        """Create a new instance of a class"""
        if not line:
            print("** class name missing **")
            return
        if line in self.classes:
            new_instance = self.classes[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show an instance by its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Show all instances of a class or all instances"""
        args = line.split()
        if not args:
            objects = storage.all()
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            objects = {k: v for k, v in storage.all().items() if args[0] in k}
        print([str(obj) for obj in objects.values()])

    def do_destroy(self, line):
        """Destroy an instance by its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """Update an instance by its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
