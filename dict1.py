# Write a Python script to sort (ascending and descending) a dictionary by value.

import random


def create_multiple_lists(name, number):
    master_dict = {}
    for i in range(number):
        master_dict.update({name+str(i): random.randint(0, 1000)})
    return master_dict


def sort_dict(master_dict):
    print((master_dict))


sort_dict(create_multiple_lists("item", 5))
