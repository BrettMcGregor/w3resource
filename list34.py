# Write a Python program using Sieve of Eratosthenes method for
# computing primes up to a specified number.
# To find all the prime numbers less than or equal to a given integer n
# by Eratosthenes' method:
#
# Create a list of consecutive integers from 2 through n:
# (2, 3, 4, ..., n).

# Initially, let p equal 2, the smallest prime number.

# Enumerate the multiples of p by counting to n from 2p in increments
# of p, and mark them in the list (these will be 2p, 3p, 4p, ...; the
# p itself should not be marked).

# Find the first number greater than p in the list that is not marked.
# If there was no such number, stop. Otherwise, let p now equal this
# new number (which is the next prime), and repeat from step 3.

# When the algorithm terminates, the numbers remaining not marked in
# the list are all the primes below n.

n = 100
list_integers = []

# Generate a list of integers then append True to each sublist
for i in range(2, n + 1):
    list_integers.append(list(range(i, i + 1)))

for item in list_integers:
    item.append(True)

# Flag non-prime numbers as False using Eratosthenes sieve
p = 2
for i in range(2, n + 1):
    for item in list_integers[i:]:
        if item[1] is True and item[0] % p == 0:
            item[1] = False
    p += 1

for result in list_integers:
    if result[1]:
        print(result[0], end=" ")
