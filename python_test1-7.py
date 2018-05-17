# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array. The element value in the i-th row and j-th
# column of the array should be i*j. Go to the editor
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form


def array(rows, columns):
    result = []
    for i in range(rows):
        sub_list = []
        for j in range(columns):
            sub_list.append(i * j)
        result.append(sub_list)
    print(result)


array(3, 5)
