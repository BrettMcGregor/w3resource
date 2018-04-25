# Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

radius = int(input("Please enter a radius and I will compute the area of the circle.\n> "))
print("The area of the circle is {}".format(math.pi*radius**2))
