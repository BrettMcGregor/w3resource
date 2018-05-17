# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input


def calc_factorial(*args):
    """
    :param args: compute the factorial of each supplied number
    :return: a comma-separated sequence of results
    """
    result = []
    for arg in args:
        answer = 1
        for i in range(1, arg + 1):
            answer = answer * i
        result.append(str(answer))
    return result


print(",".join(calc_factorial(5, 8, 23)))
