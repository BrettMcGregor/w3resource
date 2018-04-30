# Write a Python function to reverses a string if
# it's length is a multiple of 4

stringa = "https://www.w3rresource.com/python-exercises"

if len(stringa) % 4 == 0:
    print("".join(stringa[-1::-1]))
else:
    print(stringa)
