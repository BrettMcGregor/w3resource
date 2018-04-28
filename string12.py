# Write a Python program to count the occurrences of each word
# in a given sentence.
"""refactor to functions at some point"""
import string

my_string = "How many times is this in this? Exactly this, how many times."

output = []

for char in my_string:
    if char not in string.punctuation:
        output.append(char)
output = ("".join(output)).split()

my_dict = {}

for word in output:
    my_dict.update({word: output.count(word)})

print("\n{:10}{}".format("Word", "Count") + "\n" + "-" * 15)

for key, value in my_dict.items():
    print("{:10}{:^5}".format(key, value))
