# Write a Python program to construct the following pattern,
# using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# 9 lines, incrementing up to 5 and down again

for j in range(5):
    print("* " * j)
for j in range(5, 0, -1):
    print("* " * j)


