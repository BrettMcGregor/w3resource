# Write a Python program to append text to a file and display the text.

with open("text.txt", "a") as file:
    file.write("\n" * 2 + "*" * 60 + "\nAppended Text\nmore text\neven more text\n")
