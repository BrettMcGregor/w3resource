# Write a Python program to check if a string contains all
# letters of the alphabet.

text = "the quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"


print(set(text) >= set(alphabet))
