# Write a Python program to check if all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

empty_list = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
dict_list = [{1, 2}, {}, {}]


def check_list(alist):
    counter = 0
    for item in alist:
        if item:
            print(False)
            counter = 0
            break
        else:
            counter += 1
    if counter > 0:
        print(True)


check_list(empty_list)
