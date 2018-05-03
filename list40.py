# Write a Python program to split a list based on first
# character of word and return only the words starting with
# that character

word_list = ['be','have', 'do','say','get','make','go','know',
             'take', 'see', 'come', 'think', 'look','want','give',
             'use','find','tell','ask', 'work','seem','feel',
             'leave','call']


def split_by_char(input_list, char):
    output_list = []
    for item in word_list:
        if item[0] == char:
            output_list.append(item)
    print("{:^3}".format(char))
    for word in output_list:
        print(word)


split_by_char(word_list, "w")
