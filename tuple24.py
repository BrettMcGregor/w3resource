# Write a Python program to count the elements in a list
# until an element is a tuple.

sample = [1, 2, 3, 4, 5, ("tuple",)]

counter = 0
for item in sample:
    if type(item) is not tuple:
        counter += 1
    else:
        break

print(counter)
