# Write a Python program to find numbers between
#  100 and 400 (both included) where each digit
# of a number is an even number. The numbers
# obtained should be printed in a comma-separated sequence.


def find_numbers():
    result = []
    for i in range(100, 401):
        _ = []
        for num in str(i):
            if num == 0:
                _.append(num)
            elif int(num) % 2 == 0:
                _.append(num)
            else:
                _ = []
                break
        if _:
            result.append("".join(_))
    print(",".join(result))


find_numbers()
