# Write a Python program to count and display the vowels of a given text.

text = "Write a Python program to count and display the vowels of a given text"
vowels = "aeiou"

for vowel in vowels:
    count = 0
    for char in text:
        if vowel == char:
            count += 1
    print("{} occurs {} times.".format(vowel, count))

print()

for vowel in vowels:
    print("{} occurs {} times.".format(vowel, text.count(vowel)))
