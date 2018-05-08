# Write a Python program to find all the values in a list are greater
#  than a specified number.

import random


def create_multiple_lists(number, length, lists_master):
    if number == 1:  # create a single list if asked to
        for j in range(length):
            lists_master.append(random.randint(0, 1000))
    else:
        for i in range(number):
            sub_list = []
            for j in range(length):
                sub_list.append(random.randint(0, 1000))
            lists_master.append(sub_list)
    print(lists_master)
    return lists_master


# Function to print a list of all numbers greater than num in the input
# list. currenty only works for single input list
def all_those_greater_than(num):
    lists_master = []
    lists_new = []
    create_multiple_lists(1, 10, lists_master)
    for value in lists_master:
        if value > num:
            lists_new.append(value)
    print(lists_new)


all_those_greater_than(500)




