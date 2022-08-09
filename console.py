#!/usr/bin/python3
"""New class inherit from cmd"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Consol for safe database."""

    prompt = '(hbnb)'

    __list_class = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_create(self, line):
        """Create classes"""
        if self.check_class_name(line):
            try:
                new = eval(line + "()")
                new.save()
                print(new.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                obj = all_objs[key]
                print(obj)
            except Exception:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                all_objs.pop(key)
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        """Show all instnaces"""
        new_list = []
        match = True
        args = shlex.split(line)
        all_objs = storage.all()
        if len(line) != 0:
            if args[0] in HBNBCommand.__list_class:
                for key, value in all_objs.items():
                    if line == key.split('.')[0]:
                        obj = all_objs[key]
                        new_list.append(obj.__str__())
            else:
                print("** class doesn't exist **")
                match = False

        else:
            for key, value in all_objs.items():
                obj = all_objs[key]
                new_list.append(obj.__str__())
        if match:
            print(new_list)

    def do_update(self, line):
        """Update console"""
        key = self.found_class_name(line)
        if key is not None:
            args = shlex.split(line)
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    if args[3][0] and args[3][-1] != '"':
                        try:
                            args[3] = int(args[3])
                        except ValueError:
                            try:
                                args[3] = float(args[3])
                            except ValueError:
                                pass

                    obj = all_objs[key]
                    obj.__dict__.update({args[2]: args[3]})
                    setattr(obj, args[2], type(
                        getattr(obj, args[2], args[3]))(args[3]))
                    obj.save()
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """Signal C+d for exit."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        sys.exit()

    def emptyline(self):
        """Overwrite method emptyline."""

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__list_class:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
            else:
                print("** class doesn't exist **")
        return None

    def precmd(self, line):
        args = line.split('.')
        if len(args) >= 2:
            if args[1].count('()') == 1:
                clas_name = args[0]
                a = args[1].replace('(', '.')
                b = a.replace(')', '.')
                c = b.split('.')
                comand = c[0]
            # print(clas_name)
            # print(comand)
            # print(argvs)
                line = str(comand + ' ' + clas_name)
            elif args[1].count('(') == 1 and args[1].count(')') == 1:
                arguments = ""
                clas_name = args[0]
                a = args[1].replace('(', '.')
                b = a.replace(')', '.')
                c = b.split('.')
                comand = c[0]
                argvs = shlex.split(c[1], '"')
                for wrd in argvs:
                    arguments = arguments + wrd

                d = str(comand + ' ' + clas_name + ' ' + arguments)
                line = d.replace(',', ' ')
                print(line)

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
