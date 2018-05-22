# Write a Python program to read last n lines of a file.


def read_last_lines(filename, lines):
    with open(filename, "r") as text_file:
        contents = text_file.readlines()[-lines:]
        for line in contents:
            print(line, end="")


read_last_lines("text.txt", 11)
