# Write a Python program to count occurrences of a substring
# in a string.

input_text = "substring in string or this string, stringstringer, stringy"
substring = "string"
count = 0
index = 0

# Solution 1: Using while loop and conditionals with slicing
while True:
    if input_text[index:].find(substring) != -1:
        count += 1
        index += input_text[index:].find(substring) + len(substring)
    else:
        if input_text[index:].find(substring) == -1:
            break
print(count)

# Solution 2: using the count method
print(input_text.count(substring))
