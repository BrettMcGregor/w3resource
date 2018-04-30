# Write a python program to count only the repeated characters in a string.

text = 'thequickbrownfoxjumpsoverthelazydog'

unique = {}
for char in set(text):
    if text.count(char) < 2:
        continue
    unique.update({char: text.count(char)})

for key, value in unique.items():
    print("The letter {} is repeated {} times".format(key, value))
