# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

user_input = input("Please enter an integer for calculation: ")

print(int(user_input) + int(user_input*2) + int(user_input*3))
