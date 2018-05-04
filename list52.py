# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"],
#  ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

a_list = ["red", "orange", "green", "blue", "white"]
b_list = ["black", "yellow", "green", "blue"]

temp_list = []


for item in a_list:
    if item not in b_list:
        temp_list.append(item)
print("a_list-b_list: {}".format(temp_list))

temp_list = []
for thing in b_list:
    if thing not in a_list:
        temp_list.append(thing)
print("b_list-a_list: {}".format(temp_list))
