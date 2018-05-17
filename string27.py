# Write a Python program to remove existing indentation from all of the lines in a given text


def strip_indent():
    text = "    this is \n\tsome\n     text\n\t\t    with indentation"
    print(text)
    for line in text.splitlines():
        print(line.lstrip())


strip_indent()
