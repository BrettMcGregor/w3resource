# Write a Python program to print the square and cube symbol in the area
# of a rectangle and volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

import math


def area_rectangle(length, width):
    area = length * width
    print("Area of rectangle is {:.2f}cm\u00b2".format(area))


def volume_cylinder(radius, height):
    volume = (math.pi) * (radius ** 2) * (height)
    print("Volume of cylinder is {:.2f}cm\u00b3".format(volume))


area_rectangle(5, 4)
volume_cylinder(3, 6)
