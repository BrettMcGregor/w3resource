# Write a Python program to lowercase first n characters in a string


text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"


def lowercase_start(text, n):
    print("".join(text[:n].lower()) + text[n:])


lowercase_start(text, 5)
