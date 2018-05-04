# Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g',
#  'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'],
#  ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n']

# split the given list at the nth element


def split_list(in_list, n):
    temp_list = []
    for i in range(0, len(in_list), n):
        temp_list.append(list(in_list[i:n + i]))
    print(temp_list)


split_list(a_list, 2)
