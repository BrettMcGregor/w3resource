# Write a Python program to compute the greatest
# common divisor (GCD) of two positive integers


def find_gcd(int1, int2):
    divisors = []
    for i in range(1, max(int1, int2)):
        if int1 % i == 0 and int2 % i == 0:
            divisors.append(i)
    print(divisors)
    for j in range(len(divisors) - 1, 0, -1):
        if divisors[j] < min(int1, int2):
            print(divisors[j])
            break


find_gcd(54, 24)
