# Write a Python program to multiply all the items in a dictionary.


dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

values = dict1.values()
product = 1

for value in values:
    product *= value

print(product)
