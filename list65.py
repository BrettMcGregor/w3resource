# Write a Python program to access dictionary keys element by index.

# First, create a list of dictionaries


def list_of_dicts():
    colours = ["red", "orange", "yellow", "green", "blue"]
    dicts_list = []
    for i in range(len(colours)):
        dicts_list.append({i + 1: colours[i]})
    return dicts_list


# list_of_dicts()


def access_dict_element(key_index, dicts_list):
    print(dicts_list)
    print("key index argument provided = {}".format(key_index))
    print(dicts_list[key_index - 1].get(key_index))


access_dict_element(3, list_of_dicts())
