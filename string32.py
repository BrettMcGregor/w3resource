# Write a Python program to print the following floating numbers with
# no decimal places.

numbers = [1.23, 2.334, -12.3342, 14.6645333, 1, -5.667]

for number in numbers:
    print("{:>3.0f}".format(number))
