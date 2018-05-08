# . Write a Python program to iterate over dictionaries using for loops

dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

for k, v in dict1.items():
    print("{:>3}{:.>7}".format(k, v))
