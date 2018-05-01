# Write a Python program to select an item randomly from a list.
import random

list_integers = [540, 986, 21, 264, 556, 689, 908, 421, 469, 536]

print(list_integers[random.randint(0, len(list_integers))])
