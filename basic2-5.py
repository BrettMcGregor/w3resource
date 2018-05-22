# Write a Python program to create the combinations of 3 digit combo
import itertools

combos = []
for num in range(1000):
    combos.append(str(num).zfill(3))
print(combos)
