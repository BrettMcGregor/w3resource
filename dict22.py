# Write a Python program to find the highest 3 values in a dictionary.

sample_dict = {1: 459, 2: 33, 3: 9009, 4: 3, 5: 11098}

values = sorted(sample_dict.values())
print(values[-3::])
