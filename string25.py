# Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as
# Caesar's cipher, the shift cipher, Caesar's code or Caesar
# shift, is one of the simplest and most widely known encryption
# techniques. It is a type of substitution cipher in which each
# letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left
# shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private
# correspondence.


def caesar_cipher(input_string, offset, state):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output_string = []
    if state == "decode":
        offset *= -1
    for char in input_string:
        if char == " ":
            output_string.append(" ")
            continue
        if char.isupper():
            if alphabet_upper.find(char) + offset > 25:
                index = alphabet_upper.find(char) - 25 + offset - 1
            else:
                index = alphabet_upper.find(char) + offset
            output_string.append(alphabet_upper[index])
        else:
            if alphabet.find(char) + offset > 25:
                index = alphabet.find(char) - 25 + offset - 1
            else:
                index = alphabet.find(char) + offset
            output_string.append(alphabet[index])
    output_string = "".join(output_string)
    print(input_string, " >{} ".format(offset), output_string)


caesar_cipher("Andrea Pepper", 7, "code")
caesar_cipher("Hukylh Wlwwly", 7, "decode")
caesar_cipher("Brett McGregor", 7, "code")
caesar_cipher("Iylaa TjNylnvy", 7, "decode")
