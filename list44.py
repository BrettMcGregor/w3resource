# Write a Python program to generate groups of consecutive
# numbers in a list.


def generate_seq(num, num_in):
    output_list = []
    for i in range(1, num + 1):
        output_list.append(list(range(i * num_in, i * num_in + num_in)))

    print(output_list)


generate_seq(5, 2)
