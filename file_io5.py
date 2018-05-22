# Write a Python program to read a file line by line and store it into a list.

with open("text.txt", "r") as text_file:
    lines_list = text_file.readlines()[:10]

    print(lines_list)
