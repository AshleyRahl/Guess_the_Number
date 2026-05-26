# Guess the Number Game

A interactive command-line game where the player competes against the computer to guess a secret number. 
This project demonstrates basic game loops, input validation, and conditional branching in Python.

## How to Play
1. **Choose your challenge:** Select a difficulty level (Easy, Medium, or Hard).
2. **Make your guess:** Enter a number based on the range provided.
3. **Get feedback:** The computer will tell you if your guess is "Too Low" or "Too High."
4. **Win:** Keep guessing until you crack the code!

## Technical Features
- **Difficulty Tiers:** Implemented variable ranges (1-10, 1-50, 1-100) using `if/elif` statements.
- **Randomization:** Utilizes the `random` module to ensure a unique experience every game.
- **Game Loop:** Employs a `while` loop to maintain the game state until the win condition is met.
- **Modular Design:** Uses a `main()` function to keep the entry point clean and organized.
- **Input Validation:** Implemented `try/except` blocks to handle `ValueError` exceptions, preventing the program from crashing if a user enters non-numeric text.

## How to Run
1. Ensure you have Python 3 installed.
2. Run the script:
   ```bash
   python guess_the_number.py