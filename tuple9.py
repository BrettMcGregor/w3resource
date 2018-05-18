# Write a Python program to find the repeated items of a tuple.

first = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 8

repeated = []
for item in first:
    if first.count(item) > 1:
        repeated.append(item)

print(set(repeated))
