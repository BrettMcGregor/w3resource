# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_string_middle(target, stringa):
    mid1 = int(len(target)/2)
    mid2 = int((len(target)/2) * -1)
    print("".join(target[:mid1] + stringa + target[mid2:]))


insert_string_middle('{{{{}}}}', 'PHP')
