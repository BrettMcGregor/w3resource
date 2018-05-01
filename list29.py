# Write a Python program to get unique values from a list.

list_integers = [540, 986, 21, 540, 986, 21, 263, 556, 689, 908, 421, 469, 536]

# Solution 1
for i in list_integers:
    if list_integers.count(i) == 1:
        print(i)

print()
# Solution 2
print(list(i for i in list_integers if list_integers.count(i) == 1))
