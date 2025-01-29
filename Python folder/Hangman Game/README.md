# Hangman Game

This is a simple Hangman game implemented in Python. The player tries to guess a randomly chosen word by suggesting letters.

## How to Play
1. Run the Python script.
2. The program will randomly select a word and display it as underscores.
3. The player inputs one letter at a time.
4. If the letter is in the word, it is revealed; otherwise, the player loses an attempt.
5. The game continues until the player guesses the word or runs out of attempts.

## Code Explanation

### 1. Choosing a Word
The function `choose_word()` selects a random word from a predefined list of words using Python's `random.choice()` function.

### 2. Displaying the Word
The function `display_word(word, guessed_letters)` constructs a string where guessed letters are shown, and unguessed ones appear as underscores (`_`).

### 3. Running the Game
- The game starts by calling `hangman()`, which initializes the word, guessed letters set, and attempts counter.
- The game enters a loop where the player is prompted to guess a letter.
- Input validation ensures only a single alphabetic character is accepted.
- If the guess is correct, it is added to the guessed letters set.
- If incorrect, the number of attempts decreases.
- The game ends when the player guesses all letters or runs out of attempts.

## Requirements
- Python 3.x

## Running the Game
To play the game, execute the script using:
```sh
python hangman.py
```

## Features
- Random word selection.
- Limited number of attempts.
- User-friendly prompts and feedback.

Enjoy the game and improve your vocabulary!
