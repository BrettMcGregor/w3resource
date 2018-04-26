# Write a Python program to compute the greatest common
# factor (GCF) of two positive integers
import math

user_input = (input("Please enter two positive integers: ")).split()

int1 = int(user_input[0])
int2 = int(user_input[1])

gcf1 = set([int1])
gcf2 = set([int2])

for i in range(1, int1 + 1):
    if int1 % i == 0:
        gcf1.add(i)

for i in range(1, int2 + 1):
    if int2 % i == 0:
        gcf2.add(i)

print(max(gcf1.intersection(gcf2)))
