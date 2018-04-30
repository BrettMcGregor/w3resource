# Write a Python program to display a number with a comma separator.

number = 24325432598
output_num = []

number = str(number)
for i in range(len(number)):
    output_num.append(number[i])
print(",".join(output_num))

print()
print("{:,}".format(int(number)))
