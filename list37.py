# Write a Python program to find common items from two lists


mixed_list = [540, "Brett", 21, ['William', 'McGregor'], 556, 689, 90]
other_list = [["Brett"], 540, ['William', 'McGregor'], 999]

common_list = []
for item in other_list:
    if item in mixed_list:
        common_list.append(item)
print(common_list)

print(list(i for i in other_list if i in mixed_list))
