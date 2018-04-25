# Write a Python program to test whether a number is within 100 of 1000 or 2000

user_num = int(input("Please enter an integer: "))

if 900 < user_num < 1100 or 1900 < user_num < 2100:
    print("The number is within 100 of 1000 or 2000")
else:
    print("The number is not within 100 of 1000 or 2000")
