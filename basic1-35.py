# Write a Python program that will return true if the two given integer values
# are equal or their sum or difference is 5

user_input = input("Please enter two positive integers: ").split()

if user_input[0] == user_input[1] \
        or int(user_input[0]) + int(user_input[1]) == 5 \
        or abs(int(user_input[0]) - int(user_input[1])) == 5:
    print(True)
else:
    print(False)
