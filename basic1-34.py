# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

user_input = input("Please enter two positive integers: ").split()

if 15 < (int(user_input[0]) + int(user_input[1])) < 20:
    print("20")
else:
    print(int(user_input[0]) + int(user_input[1]))
