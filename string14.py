# Write a Python program that accepts a comma separated sequence of
# words as input and prints the unique words in sorted form
# (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

# Bonus: print duplicate words sorted at the end of the list of unique
# words. Expected result: black, green, red, white, black, red

string_a = "red, white, black, red, green, black"

print(", ".join(sorted(set(string_a.replace(string_a[string_a.find(" ")], "").split(",")))))
