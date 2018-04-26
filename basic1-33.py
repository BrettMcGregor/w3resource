# Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.

user_input = input("Please enter three positive integers: ").split()

if user_input[0] in user_input[1:] or user_input[1] == user_input[2]:
    print("0")
else:
    print(int(user_input[0]) + int(user_input[1]) + int(user_input[2]))
