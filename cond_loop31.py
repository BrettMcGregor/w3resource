# Write a Python program to calculate a dog's age in human years.
# Note: For the first two years, a dog year is equal to 10.5 human
#  years. After that, each dog year equals 4 human years.
# Expected Output:
#
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73


def dog_age(dog_years):
    if dog_years <= 2:
        dog_human = dog_years * 10.5
    else:
        dog_human = ((dog_years - 2) * 4) + 21
    return dog_human


print(dog_age(12))
