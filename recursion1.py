# Write a Python program to calculate the sum of a list of numbers


def recursive_sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + recursive_sum(num_list[1:])


def rec_sum(n):
    if n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)



print(recursive_sum([1,2,3,4,5,6,7,8,9]))
print(rec_sum(9))
print("correct answer is:", (9+8+7+6+5+4+3+2+1))
