# Write a Python program to create a list of empty dictionaries.


def list_of_empty_dicts(n):
    dicts_list = []
    for i in range(n):
        dicts_list.append({})
    print(dicts_list)
list_of_empty_dicts(5)

