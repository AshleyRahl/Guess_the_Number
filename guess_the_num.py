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
        # Ask user to guess and convert to integer
        guess = int(input(f"Guess a number between 1 and {x}: ")) 
        
        # Check if the user's guess is too low, high or correct
        if guess < random_number: # if user guess too low
            print("Sorry, guess again. Too Low!")
        elif guess > random_number: # if user guess too high
            print("Sorry, guess again. Too High!")
        
    # If the user guess correctly, break the loop and print congrats message
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

def main():
    print("Welcome to the Guess the Number Game!\n")
    print("I am thinking of a number between 1 and 10.")
    guess(10)


main() # Call the main function - to Start the game
      