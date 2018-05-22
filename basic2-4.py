# Write a Python program to find unique triplets
# whose three elements gives the sum of zero from
# an array of n integers?


numbers = [1, -6, 4, 2, -1, 2, 0, -2, 0]


def unique_triplet(array):
    i, j, k = (0, 1, 2)
    result = []

    while k + 1 <= len(array):
        if sum(array[i:k+1]) == 0 and\
                abs(array[i]) != abs(array[j]) != abs(array[k]) != abs(array[i]):
            result.append(tuple(array[i:k+1]))
            i += 1
            j += 1
            k += 1
        else:
            i += 1
            j += 1
            k += 1
    print(result)


unique_triplet(numbers)
