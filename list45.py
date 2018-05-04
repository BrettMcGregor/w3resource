# Write a Python program to convert a pair of values into a
# sorted unique array.

pairs_list = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
              (7, 8), (9, 10)]

output = []
for item in pairs_list:
    var1, var2 = item
    output.append(var1)
    output.append(var2)
output = list(set(output))
print(output)
