# Write a Python program to remove and print
# every third number from a list of numbers
# until the list becomes empty.


def remove_nums(int_list):
    j = 2
    while j > 0:
        if j > len(int_list):
            j -= len(int_list)
        elif len(int_list) == 1:
            print(int_list.pop(0))
            break
        else:
            print(int_list.pop(j))
            j += 2


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_nums(numbers)
