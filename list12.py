# Write a Python program to print a specified list after
# removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue']
# Expected Output : ['Green', 'White', 'Black', 'Blue']

text = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue']

print(list(i for i in text if text.index(i) not in (0, 4, 5)))
