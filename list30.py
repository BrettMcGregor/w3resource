# Write a Python program to get the frequency of the elements in a list.

list_integers = [540, 986, 21, 540, 986, 21, 263, 556, 689, 908, 421, 469, 536]

# Solution 1
for i in list_integers:
    print(i, end=",")
    print(list_integers.count(i))

# Solution 2
print("\n", list(list_integers.count(i) for i in list_integers))
