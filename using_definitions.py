"""
Program(s): using_definitions.py, definitions package, set_ops.py, dictionary_ops.py, greeting.py
Author: Jessie Horvath
Date Modified: 3/15/2022

The purpose of this program is to call three different modules
from the package "definitions" and utilize them.
"""

import definitions.dictionary_ops as dops
import definitions.greeting as hello
import definitions.set_ops as sops

if __name__ == '__main__':
    sample_dict = {"Jessie":"5 stars", "Katie": "2 stars", "Joey":"4 stars", "Jim":"1 star"}
    string = "lettuce onion tomatoes cheese"
    sample_set = set(string.split(" "))

    print(dops.print_dict(sample_dict))
    print(sops.print_set(sample_set))
    print(hello.author())
    print(hello.greeting())