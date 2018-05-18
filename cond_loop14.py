# Write a Python program that accepts a string and
# calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2


string = "Python 3.2"

digits = 0
letters = 0
for char in string:
    if char.isnumeric():
        digits += 1
    else:
        if char.isalpha():
            letters += 1
print("Letters ", letters)
print("Digits ", digits)
