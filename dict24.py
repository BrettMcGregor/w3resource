# Write a Python program to create a dictionary
# from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output:{'3': 1, 's': 1, 'r': 2, 'u': 1,
#  'w': 1, 'c': 1, 'e': 2, 'o': 1}

sample_string = 'w3resource'

# Solution
# sample_list = []
# for letter in sample_string:
#     x, y = letter, sample_string.count(letter)
#     sample_list.append((x, y))
#
# output_dict = {}
#
# for tup in set(sample_list):
#     letter, count = tup
#     output_dict.update({letter: count})
#
# print(output_dict)

# Refactored solution = better
output_dict2 = {}

for letter in sample_string:
    letter, count = letter, sample_string.count(letter)
    output_dict2.update({letter: count})

print(output_dict2)
