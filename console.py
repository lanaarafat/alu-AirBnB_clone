#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from shlex import split
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel",
               "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    do_EOF = do_quit

    def do_create(self, line):
        """creates an object"""
        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_object = eval(line)()
        print(new_object.id)
        new_object.save()

    def do_show(self, line):
        """shows an object"""
        if not line:
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key_value = strings[0] + '.' + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[key_value])

    def do_destroy(self, line):
        """deletes an object"""
        if not line:
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key_value = strings[0] + '.' + strings[1]
        if key_value not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[key_value]
        storage.save()

    def do_all(self, line):
        """prints all"""
        if not line:
            print([obj for obj in storage.all().values()])
            return
        strings = split(line)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([obj for obj in storage.all().values()
               if strings[0] == type(obj).__name__])

    def do_count(self, line):
        """Count instances of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instances = storage.all(args[0])
        count = len(instances)
        print(count)

    def do_update(self, line):
        """Update an instance based on its ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all(args[0])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        setattr(instances[key], args[2], args[3])
        storage.save()

    def default(self, line):
        """defaults"""
        sub_args = self.stripper(line)
        strings = list(shlex.shlex(line, posix=True))
        if strings[0] not in HBNBCommand.classes:
            print("*** Unknown syntax: {}".format(line))
            return
        if strings[2] == "all":
            self.do_all(strings[0])
        elif strings[2] == "count":
            count = 0
            for obj in storage.all().values():
                if strings[0] == type(obj).__name__:
                    count += 1
            print(count)
            return
        elif strings[2] == "show":
            key = strings[0] + " " + sub_args[0]
            self.do_show(key)
        elif strings[2] == "destroy":
            key = strings[0] + " " + sub_args[0]
            self.do_destroy(key)
        elif strings[2] == "update":
            new_dict = self.dict_strip(line)
            if type(new_dict) is dict:
                for key, val in new_dict.items():
                    key_val = strings[0] + " " + sub_args[0]
                    self.do_update(key_val + ' "{}" "{}"'.format(key, val))
            else:
                key = strings[0]
                for arg in sub_args:
                    key = key + " " + '"{}"'.format(arg)
                self.do_update(key)
        else:
            print("*** Unknown syntax: {}".format(line))
            return

    def stripper(self, st):
        """strips that line"""
        new_string = st[st.find("(")+1:st.rfind(")")]
        new_string = shlex.shlex(new_string, posix=True)
        new_string.whitespace += ','
        new_string.whitespace_split = True
        return list(new_string)

    def dict_strip(self, st):
        """tries to find a dict while stripping"""
        new_string = st[st.find("(")+1:st.rfind(")")]
        try:
            new_dict = new_string[new_string.find("{")+1:new_string.rfind("}")]
            return eval("{" + new_dict + "}")
        except:
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
