# Write a Python program to create all possible
# strings by using 'a', 'e', 'i', 'o', 'u'.
# Use the characters exactly once

import itertools

vowels = 'aeiou'
result = []
for item in itertools.permutations(vowels):
    result.append("".join(item))
print(result)
