# Write a Python program that will accept the base and height of a triangle
# and compute the area.

user_input = input("Please enter base and height of triangle: ")

base, height = tuple(user_input.split())

print("area of triangle equals {}".format(1/2 * int(base) * int(height)))
