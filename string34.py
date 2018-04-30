# Write a Python program to print the following integers with '*'
# on the right of specified width

numbers = [1.23, 2.334, -12.3342, 14.6645333, 1, -5.667]

for number in numbers:
    print("{:*<10.2f}".format(number))