# Write a Python program to reverse words in a string.

text = "Brett McGregor wrote this program"

output = text.split()

print(" ".join(output[-1::-1]))
