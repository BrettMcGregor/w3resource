# Write a Python program to create multiple lists.
import random


def create_list(name, length, lists_dict, i):
    sub_list = []
    for j in range(length):
        sub_list.append(random.randint(0, 1000))
    lists_dict.update({name+str(i): sub_list})



def create_multiple_lists(name, number, length):
    lists_dict = {}
    for i in range(number):
        create_list(name, length, lists_dict, i)
        name = "".join(name)
    for item in lists_dict.items():
        print(item)


create_multiple_lists("new_list", 20, 10)
