# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

input_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40], [40], [40], [40]]

for i in range(len(input_list) - 1, 0, -1):
    if input_list[i] in input_list[:i]:
        del input_list[i]
print(input_list)
