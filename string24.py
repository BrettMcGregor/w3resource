# Write a Python program to check whether a string starts with
# specified characters


def string_begins_with(the_string, characters):
    if the_string[:len(characters)] == characters:
        print(True)
    else:
        print(False)


string_begins_with("Python", "Pyr")
