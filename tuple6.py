# Write a Python program to convert a tuple to a string.

first = (1, 2, "Brett")

first = str(first)
print(type(first))
print(first)

second = (3, 4, "McGregor")

print(type("".join(str(second))))
print("".join(str(second)))
