# Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

text = "32.054,23"
output = []

for i in range(len(text)):
    if text[i] == ".":
        output.append(",")
    elif text[i] == ",":
        output.append(".")
    else:
        output.append(text[i])

print("".join(output))
