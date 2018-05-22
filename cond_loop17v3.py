letters = {'a': " ***\n*   *\n*   *\n*****\n*   *\n*   *\n*   *",
           'b': "****\n*   *\n*   *\n*   *\n*****\n*   *\n*   *\n*   *\n****"
           }

raw_input = input("Type a word: ")

for letter in raw_input:
    print(letters[letter.lower()])

