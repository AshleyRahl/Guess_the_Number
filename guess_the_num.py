"""
Guess the Number Game
This is a simple command-line game where the user/player tries to guess a randomly generated number within a certain range.
A game where you need to guess a randomly generated number.
"""

import random # Import the random module to generate random numbers

def guess(x):
    # Give me a random number between 1 and x
    random_number = random.randint(1, x)

    guess = 0

    # While users guess is not the random number keep looping till user guess corectally
    while guess != random_number: 
        guess = input(f"Guess a number between 1 and {x}: ")
        print(guess)

guess(10)        