# Write a Python program to read first n lines of a file.

with open("text.txt", "r") as text_file:
    for i in range(10):
        contents = text_file.readline()
        print(contents, end="")
