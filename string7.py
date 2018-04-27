# Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'poor' follows the 'not', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'

string = "The lyrics is not that poor!"
if string.find("not") == -1 or string.find("poor") == -1:
    print("")
else:
    if string.find("not") < string.find("poor"):
        print(string.replace(string[string.find("not"): string.find("poor") + 4], "good"))
