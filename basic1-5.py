# Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them?

username = input("Please enter your first and last name: ").split()
print(username[1] + " " + username[0])
