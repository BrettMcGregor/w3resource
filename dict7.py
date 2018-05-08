# Write a Python script to print a dictionary where the keys are
# numbers between 1 and 15 (both included) and the values are
# square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


def dict_squares(low, high, power):
    my_dict = {}
    for i in range(low, high + 1):
        my_dict.update({i: i ** power})
    print(my_dict)


dict_squares(1, 15, 2)
