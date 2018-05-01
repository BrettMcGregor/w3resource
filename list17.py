# Write a Python program to generate and print a list except
# for the first 5 elements, where the values are square of numbers
# between 1 and 30 (both included)

squares_list = []

for i in range(1, 30):
    squares_list.append(i ** 2)
new_list = squares_list[6:]
print(new_list)
