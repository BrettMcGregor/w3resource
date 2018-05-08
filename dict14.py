# Write a Python program to sort a dictionary by key.

adict = {'red': 'x#FF0000', 'green': 'y#008000', 'blue': 'z#0000FF'}

print(sorted(adict.items(), key=lambda x: x[1]))
