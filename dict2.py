# Write a Python script to add a key to a dictionary. Go to the editor
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

start_dict = {0: 10, 1: 20}


def update_dict(key, value):
    start_dict.update({key: value})
    if input("Enter another record? (Y/n) > ").upper() == "Y":
        update_dict(input("Enter key: "), input("Enter value: "))
    else:
        print(start_dict)


update_dict(input("Enter key: "), input("Enter value: "))
