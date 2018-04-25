# Write a Python program to test whether a passed letter is a vowel or not.

user_str = input("Please enter a letter: ")

vowels = frozenset("aeiou")

for char in user_str:
    if char in vowels:
        print("vowel")
    else:
        print("consonant")
