# Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

list_a = [10, 20, 30]
list_b = [40, 50, 60]

list_a.extend(list_b)
print(list_a)
