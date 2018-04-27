# Write a Python program to remove the characters which have
# odd index values of a given string.

string = "Brett McGregor"

# Solution 1

for i in range(0, len(string), 2):
    print("".join(string[i]), end = "")

print("")

# Solution 2

print(string[0::2])
