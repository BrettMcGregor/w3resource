# With a given integer number n, write a program to generate a dictionary
# that contains (i, i*i) such that is an integer number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Consider use dict()


def generate_squares(n):
    """Generate a dictionary containing range(1, n) entries with number squared as value

    :param n: upper end of range for generating dictionary populated with i: i*i
    :return:
    """
    result = {}
    for i in range(1, n + 1):
        result.update({i: i * i})
    return result


print(generate_squares(8))
