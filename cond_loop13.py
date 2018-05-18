# Write a Python program which accepts a sequence of
# comma separated 4 digit binary numbers as its input
# and print the numbers that are divisible by 5 in a
# comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


bin_list = ("0100", "0011", "1010", "1001", "1100", "1001", "1111")
result = []
for item in bin_list:
    # print(int(item, 2))
    if int(item, 2) % 5 == 0:
        result.append(item)

print("\n" + ",".join(result))
