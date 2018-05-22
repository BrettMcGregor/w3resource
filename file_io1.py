# Write a Python program to read an entire text file.

with open("text.txt", "r") as text_file:
    contents = text_file.read()
    print(contents)
