# Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

new_dict = {}

for i in range(len(keys)):
    new_dict.update({keys[i]: values[i]})

print(new_dict)
