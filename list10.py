# Write a Python program to find the list of words that are
# longer than n from a given list of words.

text = ['Write', 'a', 'Python', 'program', 'to', 'find', 'the', 'list', 'of', 'words', 'that', 'are', 'longer', 'than', 'n', 'from', 'a', 'given', 'list', 'of', 'words']


def longer(words, length):
    long_words = []
    for word in text:
        if len(word) > length:
            long_words.append(word)
    print(long_words)


longer(text, 4)
