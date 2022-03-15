"""
Program: use_my_definitions.py
Author: Jessie Horvath
Date Modified: 3/15/2022

The purpose of this program is to import the module my_definitions
and call the functions and variables from it.
"""

import my_definitions as defs

if __name__ == '__main__':
    print(defs.friendly_greeting())
    print(defs.print_author())
    print(defs.print_dict(defs.test_dict))
    print(defs.print_set(defs.test_set))