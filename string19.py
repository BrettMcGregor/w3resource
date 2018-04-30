# Write a Python program to get the last part of a string before a
# specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

stringa = "https://www.w3resource.com/python-exercises"
char = "-"

print("".join(stringa[stringa.find("-") + 1:]))
