# Write a Python program to find the list in a list of lists
# whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

list_of_lists = [[22, 4, 15], [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

greatest = 0
index = 0
i = 0
for item in list_of_lists:
    if sum(item) > greatest:
        greatest = sum(item)
        index = i
    i += 1

print(list_of_lists)
print("index {}".format(index), "sum =", greatest)
print(list_of_lists[index])
