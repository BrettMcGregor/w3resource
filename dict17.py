# Write a Python program to remove duplicates from Dictionary


dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 25, 7: 1}

keys = dict1.keys()
values = dict1.values()

dict2 = {}

for k, v in dict1.items():
    if v not in dict2.values():
        dict2[k] = v

print(dict2)
