"""
Guess the Number Game
This is a simple command-line game where the user/player tries to guess a randomly generated number within a certain range.
A game where you need to guess a randomly generated number.

This computer holds a secret number and you need to guess it.
You can choose the difficulty level to make it more fun and challenging.
"""

import random # Import the random module to generate random numbers

def guess(x):
    # Give me a random number between 1 and x
    random_number = random.randint(1, x)

    guess = 0

    # While users guess is not the random number keep looping till user guess corectally
    while guess != random_number: 
        # Ask user to guess and convert to integer
        guess = int(input(f"Guess a number: ")) 
        
        # Check if the user's guess is too low, high or correct
        if guess < random_number: # if user guess too low
            print("Sorry, guess again. Too Low!")
        elif guess > random_number: # if user guess too high
            print("Sorry, guess again. Too High!")
        
    # If the user guess correctly, break the loop and print congrats message
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

def main():
    # Welcome message and instructions for the game
    print("\n --- Welcome to Guess the Number Game! ---\n")
    print("This computer holds a secret number and you need to guess it.\n")
    print("Difficulty Level:\n" \
        "1. Easy - between 1 and 10\n" \
        "2. Medium - between 1 and 50\n" \
        "3. Hard - between 1 and 100\n")

    # Ask user to choose the game difficulty level
    difficulty = int(input("Choose difficulty Level (1-3): "))
    print()
    
    if difficulty == 1: # Easy level - between 1 and 10
        print("I am thinking of a number between 1 and 10.")
        guess(10)
    elif difficulty == 2: # Medium level - between 1 and 50
        print("I am thinking of a number between 1 and 50.")
        guess(50)
    elif difficulty == 3: # Hard level - between 1 and 100
        print("I am thinking of a number between 1 and 100.")
        guess(100)


main() # Call the main function - to Start the game
      