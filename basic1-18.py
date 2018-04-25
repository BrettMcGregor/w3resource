# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

user_num = input("Please enter three integers, separated by spaces: ")
user_num = user_num.split()

if user_num[0] == user_num[1] == user_num [2]:
    print((int(user_num[0]) + int(user_num[1]) + int(user_num [2]))*3)
else:
    print((int(user_num[0]) + int(user_num[1]) + int(user_num [2])))
