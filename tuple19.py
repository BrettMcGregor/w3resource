# Write a Python program to convert a
# list of tuples into a dictionary


first = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

the_dict = {}

for item in first:
    the_dict.update({item[0]: item[1]})

print(the_dict)



