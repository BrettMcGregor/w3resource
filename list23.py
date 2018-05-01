# Write a Python program to flatten a shallow list.

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# new_list = original_list[0] + original_list[1] + original_list[2] + original_list[3]
new_list = []
for i in range(len(original_list)):
    new_list += original_list[i]

print(new_list)
