# Write a Python program to change the position of every n-th value with
# the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

input_list = [0, 1, 2, 3, 4, 5, 6, 7]
output_list = []

if len(input_list) % 2 != 0:
    print("odd number of list elements, must be multiple of two")
else:
    for i in range(0, len(input_list), 2):
        output_list.append(input_list[i + 1])
        output_list.insert(i + 1, input_list[i])
    print(output_list)
 