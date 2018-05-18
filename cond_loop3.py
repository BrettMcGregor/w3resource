# . Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt
# appears again until the guess is correct,
# on successful guess, user will get a "Well guessed!"
# message, and the program will exit.
import random


def guess_number():
    number = random.randint(0, 9)
    print(number)
    guess = input("Guess my number between 1 and 9.\n> ")
    while True:
        if int(guess) == number:
            print("Well guessed!")
            break
        else:
            guess = input("Not my number. Please try again.\nGuess my number between 1 and 9\n> ")


guess_number()
