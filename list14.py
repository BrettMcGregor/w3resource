# Write a Python program to print the numbers of a
# specified list after removing even numbers from it.

list_integers = [540, 986, 21, 264, 556, 689, 908, 421, 469, 536]

print(list(i for i in list_integers if i % 2 != 0))
