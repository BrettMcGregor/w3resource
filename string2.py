# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# Solution 1: using .count() method and comprehensions
string = "google.com"
print({i: string.count(i) for i in string})

# Solution 2: using for loops with counter
result = {}

for i in string:
    counter = 0
    for j in string:
        if i == j:
            counter += 1
            result.update({i: counter})
print(result)

# Solution 3: using count method and for loop
for i in string:
    result.update({i: string.count(i)})
print(result)


# Solution 4: using dictview
for j in string:
    if j in result.values():
        counter += 1
        result.update({j: counter})
print(result)
