# Write a Python program to generate all sublists of a list.

list_integers = [540, 986, 21, 263, 556, 689, 908, 421, 469, 536]

sublist = []
for i in range(len(list_integers) + 1):
    for j in range(len(list_integers) + 1):
        if not list_integers[i:j]:
            continue
        sublist.append(list_integers[i:j])
print(sublist)
