"""
Project: Guess the Number Game
Version: 1.2.0
Author: AC Rahl
Description: 
    A terminal-based game where the user need to guess the randomly generated number by the computer. 
    User can choose the difficulty level to make it more fun and challenging. 
    The program uses a while loop and conditional logic to provide feedback until the correct number is guessed.
"""

import random # Import the random module to generate random numbers

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
        elif feedback != "c":
            # if user input is not "c", "h" or "l"
            print("Invalid input! Please enter 'H', 'L', or 'C'.")

    print(f"\nYay, the computer guessed your number, {guess}, correctly!")

def main():
    # Welcome message and instructions for the game
    print("\n --- Welcome to Guess the Number Game! ---\n")
    print("Let the computer guess your number you are thinking of!\n")
    print("Please choose a range for the computer to guess (the maximum number). \nThe computer will guess a number between 1 and your chosen maximum number.\n")
    # Ask user to choose the range for the computer to guess (the maximum number)
    x = int(input("Computer, I'm thinking of a number between 1 and : "))

    print("\nPlease provide feedback to the computer's guesses by typing:\n'H' for too high \n'L' for too low \n'C' for correct\n")
    computer_guess(x) # Call the computer_guess function with the user's chosen range


main() # Call the main function - to Start the game
      