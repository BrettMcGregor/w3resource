# Write a Python program to find missing and additional values
# in two lists.
# Sample data : [a, b, c, d, e, f], [d, e, f ,g h,]
# Missing values in second list: b,a,c
# Additional values in second list: g,h

first_list = ['a', 'b', 'c', 'd', 'e', 'f']
second_list = ['d', 'e', 'f', 'g', 'h']

print(set(first_list).difference(set(second_list)))
print(set(second_list).difference(set(first_list)))
