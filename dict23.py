# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}

sample_list = [{'item': 'item1', 'amount': 400},
               {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}]


output_dict = {}


for item in sample_list:
    if item['item'] not in output_dict:
        output_dict.update({item['item']: item['amount']})




print(output_dict)



