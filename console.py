#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from shlex import split
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles End of File"""
        return True

    def emptyline(self):
        """Handles empty lines"""
        pass

    def do_create(self, line):
        """Creates an object"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_object = eval(args[0])()
        new_object.save()
        print(new_object.id)

    def do_show(self, line):
        """Shows an object"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if obj_key in all_objects:
            print(all_objects[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an object"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if obj_key in all_objects:
            del all_objects[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all objects or all objects of a specific class"""
        args = line.split()
        all_objects = storage.all()
        obj_list = []
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, value in all_objects.items():
            if not args or args[0] == value.__class__.__name__:
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, line):
        """Updates an object with new information"""
        if not line:
            print("** class name missing **")
            return
        args = split(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if obj_key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objects[obj_key], args[2], args[3])
        storage.save()

    def do_count(self, line):
        """Counts the number of instances of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        count = 0
        for key in all_objects:
            if key.startswith(args[0] + "."):
                count += 1
        print(count)

    def default(self, line):
        """Handles default commands"""
        args = split(line)
        if args[0] not in HBNBCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if len(args) > 1 and args[1] == ".all()":
            self.do_all(args[0])
        elif len(args) > 2 and args[1] == ".count()":
            self.do_count(args[0])
        elif len(args) > 3 and args[1] == ".show(":
            self.do_show(args[0] + " " + args[2][1:-2])
        elif len(args) > 3 and args[1] == ".destroy(":
            self.do_destroy(args[0] + " " + args[2][1:-2])
        elif len(args) > 3 and args[1] == ".update(":
            update_args = args[3][1:-2].replace(",", "").split()
            update_line = "{} {} {} {}".format(args[0], args[2][1:-2], update_args[0], update_args[1])
            self.do_update(update_line)
        else:
            print("*** Unknown syntax: {}".format(line))

    def stripper(self, st):
        """Strips that line"""
        new_string = st[st.find("(")+1:st.rfind(")")]
        new_string = shlex.shlex(new_string, posix=True)
        new_string.whitespace += ','
        new_string.whitespace_split = True
        return list(new_string)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
