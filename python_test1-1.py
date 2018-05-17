# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.


def find_numbers(start, stop, divisible, not_multiple):
    """
    :param start: start of search range
    :param stop: end of search range
    :param divisible: find numbers which are divisible by this number
    :param not_multiple: exclude numbers that are a multiple of this number
    :return: list of numbers meeting above criteria
    """
    result = []
    for i in range(start, stop + 1):
        if i % divisible == 0 and i % not_multiple != 0:
            result.append(i)
    return result


print(find_numbers(2000, 3200, 7, 5))
print(find_numbers(0, 100, 7, 5))
