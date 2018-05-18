# Write a Python program to remove empty value from tuples in a list.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

first = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

second = []
for item in first:
    if item:
        second.append(item)

print(second)
