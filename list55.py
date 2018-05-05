# Write a Python program to remove key values pairs from a
# list of dictionaries


list_of_dicts = [{'key1': 'value1', 'key2': 'value2'},
                 {'key1': 'value3', 'key2': 'value4'}]


for item in list_of_dicts:
    del item['key1']

print(list_of_dicts)

