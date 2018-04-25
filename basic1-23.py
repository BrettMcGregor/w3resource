# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

n = 5
user_str = input("Please enter a string: ")

if len(user_str) < 2:
    print(user_str * n)
else:
    print((user_str[0]+user_str[1]) * n)
