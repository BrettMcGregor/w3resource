# Write a Python function that takes a list of words and returns the
# length of the longest one.

words = ("Write a Python function that takes a list of words and").split()
lengths = []

for word in words:
    lengths.append(len(word))
print(max(lengths))
