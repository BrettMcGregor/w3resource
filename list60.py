# Write a Python program to find a tuple, with the smallest second
# value from a list of tuples.

list_tuples = [(4, 1), (1, 2), (6, 0), (5, 8), (12, 9)]

print(sorted(list_tuples, key=lambda n: (n[1]))[0])
