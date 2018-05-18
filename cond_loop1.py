# Write a Python program to find those numbers
# which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).


def find_numbers(divisible, multiple, start, stop):
    """

    :param divisible: divisible by this number
    :param multiple: multiple of this number
    :param start: start of search
    :param stop: end of search
    :return: result
    """
    result = []
    for i in range(start, stop + 1):
        if i % divisible == 0 and i % multiple == 0:
            result.append(i)
    return result


print(find_numbers(7, 5, 1500, 2700))
