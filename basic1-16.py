# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

user_num = int(input("Please enter an integer: "))

if user_num > 17:
    print(abs(user_num - 17) * 2)
else:
    print(abs(user_num - 17))
