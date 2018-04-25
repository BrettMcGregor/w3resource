# Write a Python program to check whether a specified value is contained in a group of values.
# Test data:
# 3 -> [1, 5, 8, 3] : True
# # -1 -> [1, 5, 8, 3] : False
#
# test = {1, 5, 8, 3}
# nums = [3, -1]

for num in [3, -1]:
    if num in [1, 5, 8, 3]:
        print(True)
    else:
        print(False)
