# Write a Python program to generate and print a list of first
# and last 5 elements where the values are square of numbers
# between 1 and 30 (both included)

squares_list = []

for i in range(1, 30):
    squares_list.append(i ** 2)
new_list = squares_list[:5] + squares_list[-5:]
print(new_list)
