from sniffer.api import *  # import the really small API
from subprocess import call
from datetime import datetime
import os  # , termstyle

# you can customize the pass/fail colors like this
# pass_fg_color = termstyle.green
# pass_bg_color = termstyle.bg_default
# fail_fg_color = termstyle.red
# fail_bg_color = termstyle.bg_default

# All lists in this variable will be under surveillance for changes.
# watch_paths = ['.', 'tests/']


@select_runnable('first')
@file_validator
def python_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')


@select_runnable('linked_list_test')
@file_validator
def linked_list_file(filename):
    return filename.endswith('linked_list.py')


@select_runnable('hash_table_test')
@file_validator
def hash_table_file(filename):
    return filename.endswith('hash_table.py')


@runnable
def linked_list_test(*args):
    print("===Linked List Test===")
    command = "nosetests tests/test_linked_list.py -v"  # nose.run(argv=['tests/test_linked_list.py', '-v'])
    return call(command, shell=True) == 0


@runnable
def hash_table_test(*args):
    print("===Hash Table Test===")
    command = "nosetests tests/test_hash_table.py -v"  # nose.run(argv=['tests/test_linked_list.py', '-v'])
    return call(command, shell=True) == 0


@runnable
def first(*args):
    print(str(datetime.now()))
    return True
