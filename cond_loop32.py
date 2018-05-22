# Write a Python program to check whether an alphabet is a
# vowel or consonant.
# Expected Output:
#
# Input a letter of the alphabet: k
# k is a consonant.


def check_letter():
    vowels = "aeiou"
    raw_input = input("Enter a letter: ")
    if raw_input in vowels:
        print("{} is a vowel".format(raw_input))
    else:
        print("{} is a consonant".format(raw_input))


check_letter()
