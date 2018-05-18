# Write a Python program to unzip a list
#  of tuples into individual lists


first = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

second = []
for item in first:
    second.append(list(item))

print(second)
