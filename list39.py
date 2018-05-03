# Write a Python program to convert a list of multiple integers into a
# single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

input_list = [11, 33, 50]
output = ""
for item in input_list:
    output = output.join(str(item))
output = int(output)

print(output)
print(type(output))
