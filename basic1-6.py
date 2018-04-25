# Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.

user_num = input("Please enter a series of integers separated with commas.\n> ")

print(list(user_num.split(",")))
print(tuple(user_num.split(",")))
