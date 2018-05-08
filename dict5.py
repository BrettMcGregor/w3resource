# Write a Python program to iterate over dictionaries using for loops.

import random


def create_multiple_lists(name, number, master_dict):
    for i in range(number):
        master_dict.update({name+str(i): random.randint(0, 1000)})
    return master_dict


def iterate_dict():
    master_dict = {}
    create_multiple_lists("item", 5, master_dict)
    for keys, values in master_dict.items():
        print(keys, values)


iterate_dict()
