"""
Program: my_definitions.py
Author: Jessie Horvath
Date Modified: 3/15/2022

The purpose of this program is to define a set of functions
that will be called in a separate file. There are also defined
variables assigned in this file.
"""

def friendly_greeting():
    return "Hello friend"

def print_author():
    return "Jessie Horvath is the author"

def print_dict(d):
    for key, value in d.items():
        print(f"{key}, {value}\n")

def print_set(set):
    for i in set:
        print(f"{i}\n")

test_dict = {"A":1, "B":2, "C":3, "D":4}
test_string = ("jumping_jacks tightrope pushups wallsits")
test_set = set(test_string.split(" "))