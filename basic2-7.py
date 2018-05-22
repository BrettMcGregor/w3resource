# Write a Python program to count the number of each character of a given text of a text file

with open("basic2-7_text", "r") as text:
    string = text.read().upper()
    result = []
    for char in set(list(string)):
        result.append((char, string.count(char)))
    print(sorted(result, key=lambda x: x[1], reverse=True))
