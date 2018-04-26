# Write a Python program to get the least common multiple (LCM)
# of two positive integers

user_input = sorted((input("Please enter two positive integers: ")).split())

int1 = int(user_input[0])
int2 = int(user_input[1])

lcm1 = []
lcm2 = []

i = 2
while True:
    lcm1.append(int1 * i)
    lcm2.append(int2 * i)
    if int1 * i in lcm2:
        print(int1 * i)
        break
    i += 1
