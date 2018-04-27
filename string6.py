# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with
# 'ing' then add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string = "string"
new_string = list(string)
if len(new_string) >= 3:
    if "".join(new_string[-3:]) == "ing":
        new_string.append("ly")
    else:
        new_string.append("ing")
print("".join(new_string))
