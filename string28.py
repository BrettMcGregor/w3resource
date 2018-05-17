# Write a Python program to add a prefix text
# to all of the lines in a string


def add_prefix():
    text = "just\nsome\nlines\nof\ntext."
    for line in text.splitlines():
        print("." * 10 + line)


add_prefix()
