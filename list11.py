# Write a Python function that takes two lists and returns
# True if they have at least one common member.

text_1 = ['abc', 'xyz', 1221, 'aba', '1221', 'abc', 'xyz', 'Brett']
text_2 = ['Brett', 1221]

for item in text_2:
    if item in text_1:
        print(True)
        break
