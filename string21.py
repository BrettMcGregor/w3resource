# Write a Python function to convert a given string to all
# uppercase if it contains at least 2 uppercase characters in the
# first 4 characters.

stringa = "HtTps://www.w3rresource.com"

count = 0
for i in range(5):
    if stringa[i].isupper():
        count += 1
if count > 1:
    print(stringa.upper())
else:
    print(stringa)
