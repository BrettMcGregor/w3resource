# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user

user_int = int(input("Please enter an integer: "))

if user_int % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
