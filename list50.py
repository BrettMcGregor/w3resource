# Write a Python program to sort a list of nested dictionaries

a_list = [{'key': {'subkey': 1}},
          {'key': {'subkey': 10}},
          {'key': {'subkey': 5}}]

print(sorted(a_list, key=lambda x: x['key']['subkey']))
