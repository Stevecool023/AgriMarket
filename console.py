#!/usr/bin/env python3

"""
AgriMarket Console
"""

import sys
sys.path.append('/home/AgriMarket/backend')
from models import storage # Import storage first
from models.user import User # Import User class
from models.product import Product
from models.equipment import Equipment
from models.transaction import Transaction
import cmd

class AMCommand(cmd.Cmd):
    """ Class AMCommand to implement the command interpreter. """
    prompt = '(agrimarket) '
    __all_117 = 0

    def emptyline(self):
        """ Do nothing on empty input. """
        pass

    def precmd(self, line):
        """ Edit given command to allow a second type of input. """
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            AMCommand.__all_117 = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argv = line.split()
            cmd_argv[0], cmd_argv[1] = cmd_argv[1], cmd_argv[1]
            line = " ".join(cmd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        """ Quit command to exit the program. """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program. """
        print()
        return True

    def do_create(self, arg):
        """ Create an object of any class with optional parameters. """
        if not arg:
            print("** class name missing **")
            return

        # Split the arguments into class name and parameters
        args = arg.split()
        class_name = args[0]

        if class_name not in AMCommand.classes:
            print("** class doesn't exist **")
            return

        params = {}
        for param in args[1:]:
            try:
                key, value = param.split('=')
                # Process the value to handle different types
                if value.startswith('"'):
                    value = value[1:].replace("_", " ")
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                params[key] = value
            except ValueError:
                pass

        new_instance = AMCommand.classes[class_name](**params)
        new_instance.save()
        print(new_instance.id)



    def do_show(self, arg):
        """ Print the string representation of an instance based on ID. """
        cmd_argv = arg.split()

        if not cmd_argv:
            print("** class name missing **")
            return

        class_name = cmd_argv[0]


        try:
            eval(class_name)
        except:
            print(f"** class {class_name} doesn't exist **")
            return

        if len(cmd_argv) < 2:
            print(f"** instance id missing **")
            return

        all_objs = storage.all()
        instance_id = cmd_argv[1]
        key = f"{class_name}.{instance_id}"

        
        if key in all_objs:
            print(all_objs[key])
        else:
            print(f"** no instance found **")

    def do_all(self, arg):
        """ Print all instances or all instances of a specific class. """
        cmd_argv = arg.split()

        if not cmd_argv:
            print("** class name missing **")
            return

        class_name = cmd_argv[0]

        if class_name not in class_map:
            print(f"** class {class_name} doesn't exist **")
            return

        all_objs = storage.all()
        print_list = []

        if len(cmd_argv) > 1:
            class_name = cmd_argv[0]
            print_list = [str(value) for key, value in all_objs.items() if key.startswith(class_name + ".")]
        else:
            print_list = [str(value) for value in all_objs.values()]


        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

    def do_destroy(self, arg):
        """
        Deletes an instance based on its ID and saves the changes
        Usage: destroy <class name> <id>
        """
        cmd_argv = arg.split()

        if not cmd_argv:
            print("** class name missing **")
            return

        class_name = cmd_argv[0]

        try:
            eval(class_name)
        except:
            print(f"** class {class_name} doesn't exist **")
            return

        all_objs = storage.all()

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return
        
        instance_id = cmd_argv[1]
        key = f"{class_name}.{instance_id}"


        if key in all_objs:
            all_objs.pop(key)
            storage.save()
        else:
            print(f"** no instance found **")


    def do_update(self, arg):
        """ 
        Updates an instance based on its ID with a given attribute and value
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        cmd_argv = arg.split()

        if not cmd_argv:
            print("** class name missing **")
            return

        class_name = cmd_argv[0]

        try:
            eval(class_name)
        except:
            print(f"** class {class_name} doesn't exist **")
            return

        all_objs = storage.all()

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return

        instance_id = cmd_argv[1]
        key = f"{class_name}.{instance_id}"

        if key in all_objs:
            if len(cmd_argv) < 3:
                print("** dictionary missing **")
                return
            try:
                dictionary = eval(" ".join(cmd_argv[2:]))
            except:
                print("** dictionary format is invalid **")
                return

            instance = all_objs[key]

            if isinstance(dictionary, dict):
                for key, value in dictionary.items():
                    if hasattr(instance, key):
                        setattr(instance, key, value)
                instance.save()
            else:
                print(f"** no instance found **")
        else:
            print(f"** no instance found **")



    def do_count(self, arg):
        """ Usage: count <class name> or <class name>.count() """
        """ Retrieve the number of instances of a class """
        cmd_argv = arg.split()

        if not cmd_argv:
            print("** class name missing **")
            return


        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        count = 0

        if len(cmd_argv) > 1:
            class_name = cmd_argv[0]
            count = sum(1 for key in all_objs if key.startswith(class_name + "."))
        else:
            print("** class name missing **")
            return
        print(count)


    def do_help(self, arg):
        """
        List available commands with 'help' or provide detailed help for a specific command.
        Usage:
            help                    - List all available commands.
            help <command>          - Display detailed help for a specific command.

        Args:
            arg (str): The command name for which you want to see detailed help.
        """
        if arg:
            # show help for a specific command
            try:
                doc = getattr(self, "help_" + arg)
                print(doc.__doc__)
            except AttributeError:
                print(f"No help available for '{arg}'")
        else:
            # List all available commands
            documented_commands = [name[3:] for name in dir(self) if name.startswith('do_')]
            documented_commands.sort()
            self.stdout.write("Documented commands (type help <command> for details):\n")
            self.stdout.write(", ".join(documented_commands) + '\n')


if __name__ == '__main__':
    AMCommand().cmdloop()
