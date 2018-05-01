# Write a Python program to print the index of the character in a string. Go to the editor
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2

text = "w3resource"

for i in range(len(text)):
    print("Current character {} at position {}".format(text[i], i))
    i += 1
