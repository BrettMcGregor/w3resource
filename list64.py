# Write a Python program to iterate over two lists simultaneously.

list1 = [1, 2, 3, 4, 5]
list2 = ["red", "orange", "yellow", "green", "blue"]

for i in list1:
    print(i, list2[i - 1])
