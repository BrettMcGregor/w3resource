# Write a Python program to create the multiplication
#  table (from 1 to 12) of a number.

for i in range(1, 13):
    for j in range(1, 13):
        print("{:3} x {:2} = {:3}".format(i, j, i * j))
