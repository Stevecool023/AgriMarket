#!/usr/bin/env python3

"""
Agricultural Website Console
"""

import cmd
import sys
from models import storage

class AMCommand(cmd.Cmd):
    """ Class AMCommand to implement the command interpreter. """
    prompt = '(agrimarket) '

    def emptyline(self):
        """ Do nothing on empty input. """
        pass

    def precmd(self, line):
        """ Edit given command to allow a second type of input. """
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program. """
        print()
        return True

    def do_create(self, arg):
        """ Create an instance if the Model exists. """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Print the string representation of an instance based on ID. """
        cmd_argv = arg.split()

        if not arg:
            print("** class name missing **")
            return

        try:
            eval(cmd_argv[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print all instances or all instances of a specific class. """
        cmd_argv = arg.split()

        if cmd_argv and cmd_argv[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        print_list = []

        for key, value in all_objs.items():
            if not cmd_argv or cmd_argv[0] == value.__class__.__name__:
                print_list.append(str(value))

        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

    def do_destroy(self, arg):
        """ Deletes an instance based on its ID. """
        cmd_argv = arg.split()

        if not arg:
            print("** class name missing **")
            return

        try:
            eval(cmd_argv[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return
        
        all_objs = storage.all()
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """ Updates an instance attribute or create it if it doesn't exist. """
        cmd_argv = arg.split()

        if not arg:
            print("** class name missing **")
            return

        try:
            eval(cmd_argv[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return

        if len(cmd_argv) < 3:
            print("** attribute name missing **")
            return

        if len(cmd_argv) < 4:
            print("** value missing **")
            return

        all_objs = storage.all()
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if key not in all_objs:
            print("** no instance found **")
            return
        
        instance = all_objs[key]
        attr_name = cmd_argv[2]
        value = cmd_argv[3]

        try:
            value = eval(value)
        except (NameError, SyntaxError):
            pass

        setattr(instance, attr_name, value)
        instance.save()

    def do_count(self, arg):
        """ Count instances of a specific class or all instances. """
        cmd_argv = arg.split()

        if not arg:
            print(len(storage.all()))
            return

        if cmd_argv[0] in storage.classes:
            count = 0
            for key in storage.all():
                if key.split('.')[0] == cmd_argv[0]:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    AMCommand().cmdloop()
