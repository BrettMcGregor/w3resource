# Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are
# same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

text = ['abc', 'xyz', 'aba', '1221']
count = 0

for item in text:
    if len(item) > 1 and item[0] == item[-1]:
        count += 1

print(count)
