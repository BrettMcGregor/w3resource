# Write a Python program to set the indentation of the first line.


def indent_first_line():
    text = "first line\nsecond line\nthird line"
    print(text.splitlines()[0])
    for i in range(1, len(text.splitlines())):
        print("\t" + text.splitlines()[i])


indent_first_line()
