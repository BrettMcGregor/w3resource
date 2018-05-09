# Write a Python program to print all unique values in a list of
# dictionaries
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
#  {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
# {"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007',
# 'S001', 'S009'}


sample_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique_values = []

for item in sample_dict:
    for v in item.values():
        if v not in unique_values:
            unique_values.append(v)

print(set(unique_values))
