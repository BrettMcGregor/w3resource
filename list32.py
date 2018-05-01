# Write a Python program to check whether a list contains a sublist.

list_integers = [[540, 986], [21, 263], [556, 689, 908, 421], [469, 536]]
check = [556, 689, 908, 421]

for item in list_integers:
    if item == check:
        print(True)
