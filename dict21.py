# Write a Python program to create and display all combinations
# of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

import itertools

sample_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

v = []


for value in sample_dict.values():
    for i in range(len(value)):
        v.append(value[i])

print(v)
print(list(itertools.permutations(v, 2)))





