# Write a Python program to insert an element before each
# element of a list.

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(a_list), 0, -1):
    a_list.insert(i - 1, "x")
print(a_list)

