# Write a Python program to count the number 4 in a given list

given_list = [1, 4, 5, 3, 44, 4, 23, 112, 2435, 4]
count = 0
print(given_list)
for num in given_list:
    if num == 4:
        count += 1
print("The number 4 appears {} times.".format(count))

# Write a Python program to count the number 4 in a given list any time that it appears

count = 0
all_nums = "".join(str(given_list))
for char in all_nums:
    if char == "4":
        count += 1
print("The number 4 actually appears {} times.".format(count))
