# Write a Python program to count the number of elements in a
# list within a specified range


def range_count(lower, upper):
    list_integers = [540, 986, 21, 263, 556, 689, 908, 421, 469, 536]
    count = 0
    for num in list_integers:
        if num in range(lower, upper):
            count += 1
    print(count)


range_count(300, 800)
