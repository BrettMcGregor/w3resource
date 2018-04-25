# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

user_string = input("Please enter a sentence string: ")

user_string_list = user_string.split()

if user_string_list[0] == "Is":
    print(user_string)
else:
    user_string_list.insert(0, "Is")
    print(" ".join(user_string_list))
