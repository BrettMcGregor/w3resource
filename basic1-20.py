# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

user_string = input("Please enter a sentence string: ")
user_int = int(input("Please enter a positive integer: "))

string_copies = user_string * user_int
print(string_copies)
