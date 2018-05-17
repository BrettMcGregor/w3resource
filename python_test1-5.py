# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class Test5:
    """
    """
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def get_string(self, name):
        self.name = input("Please enter a string: ")

    def print_string(self, name):
        print(Test5.get_string())


print(Test5.print_string())
