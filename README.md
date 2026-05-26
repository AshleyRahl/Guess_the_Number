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

---

# Guess the Number (Computer Edition)

In this version of the game, the tables are turned! You think of a number, and the computer tries to guess it.

## 🧠 The Logic: Binary Search Principles
This project demonstrates **Dynamic Range Adjustment**. Every time you tell the computer its guess is too high or too low, it updates its boundaries:
* **If Too High:** The computer sets its `maximum` to `guess - 1`.
* **If Too Low:** The computer sets its `minimum` to `guess + 1`.


## 🚀 Technical Features
- **Inverse Logic:** Instead of tracking user attempts, the program manages stateful `low` and `high` variables to narrow down the search space.
- **Dynamic Range:** The user decides how large the "search field" is (e.g., 1 to 1000).
- **Feedback Loop:** Uses a `while` loop that persists until the "Correct" signal is received.

## 🏃 How to Run
```bash
python computer_guess.py