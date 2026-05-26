"""
Project: Guess the Number (Computer Guesser)
Version: 1.2.0
Author: AC Rahl
Description: 
    A reverse guessing game where the user thinks of a number and 
    provides feedback (High/Low/Correct) to the computer. 
    The computer uses dynamic range adjustment to narrow down 
    the possibilities and find the user's secret number.
"""

import random # Import the random module to generate random numbers

# User will guess the number the computer is thinking of
def player_guess(x):
    # Give me a random number between 1 and x
    random_number = random.randint(1, x)

    guess = 0

    # While users guess is not the random number keep looping till user guess corectally
    while guess != random_number: 
        # Add a try-except block to handle non-integer inputs and program from crashing
        try:
            # Ask user to guess and convert to integer
            guess = int(input(f"Guess a number: ")) 
            
            # Check if the user's guess is too low, high or correct
            if guess < random_number: # if user guess too low
                print("Sorry, guess again. Too Low!")
            elif guess > random_number: # if user guess too high
                print("Sorry, guess again. Too High!")
        # 
        except ValueError:
            print("Invalid input! Please enter a numerical number (e.g., 1).")
            continue # Skip the rest of the loop and prompt user to guess again
        
    # If the user guess correctly, break the loop and print congrats message
    print(f"\nYay, congrats. You have guessed the number {random_number} correctly!")

# Computer will guess the number the user is thinking of
def computer_guess(x):
    # Giving the computer a range to work with (a minimum and maximum number)
    low = 1 # Minimum number for computer to work with
    high = x # Maximum number for computer to work with
    feedback = "" # Variable to store user's feedback on computer's guess - "h" for too high, "l" for too low, "c" for correct

    # While the computer's guess is not correct ("c"), keep looping and adjusting the range based on user's feedback
    while feedback != "c":
        if low != high:
            # Computer makes a guess within the current range
            # Between low and high, computer will randomly guess a number
            # Range between the updated min and max number
            guess = random.randint(low, high) 
        else:
            guess = low # could also be high since low and high are equal
        # Computer makes a guess and askuser for feedback
        # lowecase the feedback to make it easier to compare
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()

        # if computer's guess is too high, adjust the high end of the range (Maximum number for computer to work with)
        if feedback == "h": 
            high = guess - 1
        # if computer's guess is too low, adjust the low end of the range (Minimum number for computer to work with)
        elif feedback == "l": 
            low = guess + 1

    print(f"\nYay, the computer guessed your number, {guess}, correctly!")


def main():
    # Welcome message and instructions for the game
    print("\n --- Welcome to Guess the Number Game! ---\n")
    print("This computer holds a secret number and you need to guess it.\n")


    print("Difficulty Level:\n" \
        "1. Easy - between 1 and 10\n" \
        "2. Medium - between 1 and 50\n" \
        "3. Hard - between 1 and 100\n")
# Keep asking until they pick a valid difficulty
    while True:
        try:
            # Ask user to choose the game difficulty level
            difficulty = int(input("Choose difficulty Level (1-3): "))
            print()
            
            # Choose range depending on user's choice
            # Call guess function based on difficalty level
            if difficulty == 1: # Easy level - between 1 and 10
                print("I am thinking of a number between 1 and 10.")
                player_guess(10)
            elif difficulty == 2: # Medium level - between 1 and 50
                print("I am thinking of a number between 1 and 50.")
                player_guess(50)
            elif difficulty == 3: # Hard level - between 1 and 100
                print("I am thinking of a number between 1 and 100.")
                player_guess(100)
            else: # This else block will execute if user input is not 1, 2 or 3
                print("Invalid choice! Please choose between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a numerical number (e.g., 1, 2 or 3).")

main() # Call the main function - to Start the game
      