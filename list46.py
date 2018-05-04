# Write a Python program to select the odd items of a list.

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(x for x in a_list if x % 2 != 0))
