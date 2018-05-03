# Write a Python program to create a list by concatenating
#  a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# # Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


def multi_list(input_list, n):
    output_list = []
    for i in range(1, n + 1):
        for item in input_list:
            output_list.append(item + str(i))
    print(output_list)

multi_list(["a", "b"], 5)
