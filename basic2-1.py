# Write a Python function that takes a sequence
# of numbers and determines if all the numbers
# are different from each other.


def check_for_duplicates():
    sequence = [1,2,9,3,4,4,4,5,6,7,8,9]
    unique = True
    for i in range(len(sequence)):
        if sequence[i] in sequence[i+1:]:
            print(sequence[i])
            unique = False
    print("All unique: " + str(unique))


check_for_duplicates()
