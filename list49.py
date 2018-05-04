# Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"],
# ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output:
# [{'color_name': 'Black', 'color_code': '#000000'},
# {'color_name': 'Red', 'color_code': '#FF0000'},
# {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


a_list = ["Black", "Red", "Maroon", "Yellow"]
b_list = ["#000000", "#FF0000", "#800000", "#FFFF00"]
c_list = []

for i in range(len(a_list)):
    c_list.append({"color_name": a_list[i],
                   "color_code": b_list[i]})
print(c_list)
