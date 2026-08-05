# Find the Gold Game

A simple Python grid-based game where players search for hidden gold on a 3×3 map. The program randomly places the gold in one of the grid's cells, and the player must guess its location by entering a row and column number (for example, `12` represents row 1, column 2). Incorrect guesses are marked on the map with an **X**, preventing the player from selecting the same location again. Once the gold is found, the program evaluates the player's performance by awarding one of three achievement levels: **Perfect**, **Average**, or **Noob**, based on the number of attempts taken.

## Features

* Generates a random gold location on a 3×3 grid.
* Allows players to guess the gold's position using row and column coordinates.
* Marks incorrect guesses with an **X** on the map.
* Prevents players from selecting the same location twice.
* Awards an achievement level based on the number of guesses.
* Demonstrates the use of lists, loops, functions, conditional statements, and Python's `random` module.

## How to Run

1. Make sure Python 3 is installed.
2. Run the script:

   ```bash
   python find_the_gold.py
   ```
3. Enter your name.
4. Guess the gold's location by entering a two-digit coordinate (e.g., `12` for row 1, column 2).
5. Continue guessing until you find the gold.

## Example

```text
Welcome to Find The Gold!

Rules:
1. You will guess the location of the gold.
2. Enter the row and column as a two-digit number (e.g., 12 = row 1, column 2).
3. Rows and columns start from 1.
4. Earn Perfect, Average, or Noob achievements based on your number of guesses.

What's your name? John

 ['■', '■', '■']
 ['■', '■', '■']
 ['■', '■', '■']

Please guess the gold : 22
You guessed it wrong!

 ['■', '■', '■']
 ['■', 'X', '■']
 ['■', '■', '■']

Please guess the gold : 31
Congratulations, John.. You guessed it correctly
You've achieved Perfect level!
Thankyou for using our program, John!
```

## Language

* Python 3
