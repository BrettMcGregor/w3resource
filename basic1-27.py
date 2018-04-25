# Write a Python program to concatenate all elements in a list into a string and return it.

the_list = [1, "hello", 12344, 4, 6, -12, "goodbye"]

for i in range(0, len(the_list)):
    the_list[i] = str(the_list[i])

print("".join(the_list))
