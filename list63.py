# Write a Python program to insert a given string at the
# beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

my_list = [1, 2, 3, 4]
my_string = "emp"

for i in range(len(my_list)):
    my_list[i] = my_string + str(my_list[i])
print(my_list)
