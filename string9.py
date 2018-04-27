# Write a Python program to remove the nth index character from
# a nonempty string.


def remove_nth(string, n):
    print(string.replace(string[n], "", 1))


remove_nth("a Python program to remove the nth index character", 12)
