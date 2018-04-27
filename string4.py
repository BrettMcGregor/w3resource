# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first
# char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = "abracadabra"

result = list(string[0])
for i in range(1, len(string)):
    if string[i] == string[0]:
        result.append("$")
    else:
        result.append(string[i])
print("".join(result))
