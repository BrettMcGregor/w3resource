# Write a Python program to check the validity of password input by users.
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
#     Maximum length 16 characters.


def validate_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    characters = "$#@"
    count_lower = False
    count_upper = False
    count_num = False
    count_char = False
    length = False

    raw_input = input("Enter a password. Min length 6. Max length 16.\n\
                        At least 1 letter between [a-z] and 1 letter between [A-Z].\n\
                        At least 1 number between [0-9].\
                        At least 1 character from [$#@]\n> ")
    for char in raw_input:
        if char in alphabet:
            count_lower = True
        elif 6 <= len(raw_input) <= 16:
            length = True
        elif char in alphabet.upper():
            count_upper = True
        elif char in characters:
            count_char = True
        elif char.isdigit():
            if int(char) in range(10):
                count_num = True

    if count_lower is True and count_upper is True and count_num is True and count_char is True and length is True:
        print("Valid password.")
    else:
        print("Invalid password.")


validate_password()
