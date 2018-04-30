# Write a Python program to print the following numbers with zeros on
# the left of the specified width

numbers = [1.23, 2.334, -12.3342, 14.6645333, 1, -5.667]

for number in numbers:
    print("{:0=+9.0f}".format(number))
