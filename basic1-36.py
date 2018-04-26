# Write a Python program to add two objects if both objects are an integer type.

object1 = "string"
object2 = 3
object3 = 6
object4 = [5, 7, 8]

def add_int(a, b):
    if isinstance(a, int) and isinstance(b, int):
        print(a + b)

add_int(object2, object3)
