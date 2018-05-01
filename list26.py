# Write a python program to check whether two lists are
# circularly identical.

import itertools

list_a = [10, 0, 0, 10, 0]
list_b = [0, 10, 0, 10, 0]

ref = list(itertools.permutations(list_a))

for item in ref:
    if list(item) == list_b:
        print(True)
        break
