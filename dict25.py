my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for key in my_dict.keys():
    print("{:^5}".format(key), end="")
print()
print("-"*15)
for k, v in my_dict.items():
    print("{:^5}".format(my_dict[k][0]), end="")
print()
for k, v in my_dict.items():
    print("{:^5}".format(my_dict[k][1]), end="")
print()
for k, v in my_dict.items():
    print("{:^5}".format(my_dict[k][2]), end="")

