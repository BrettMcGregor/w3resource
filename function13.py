# Write a Python function that prints out the first n rows of
# Pascal's triangle.
# Note : Pascal's triangle is an arithmetic and geometric
# figure first imagined by Blaise Pascal.
#
# Sample Pascal's triangle :
# Pascal's triangle
#
# Each number is the two numbers above it added together


def pascals_triangle(n=3):
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        new_row = [1, 1]
        for j in range(len(triangle[-1]) - 1):
            new_row.insert(-1, triangle[-1][j] + triangle[-1][j + 1])
        triangle.append(new_row)
    for row in triangle:
        print("{:^40}".format("".join(str(row))))


pascals_triangle(10)
