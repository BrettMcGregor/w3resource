# Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty
# tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# define the keyword to use sorted() function to sort tuple on last value
def last(n):
    return n[-1]


print(sorted(tuple_list, key=last))
