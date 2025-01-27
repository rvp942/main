# Number Guessing Game

This is a simple terminal-based number guessing game built with Python. The program generates a random number between 1 and 100, and the player has to guess it.

## Features
- Randomly generates a number between 1 and 100.
- Provides feedback if the guess is too low or too high.
- Tracks the number of attempts.
- Allows the player to quit the game by typing `exit`.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Save the script as `number_guessing_game.py` or download it from the repository.
2. Ensure Python 3 is installed on your machine.
3. Run the script in a terminal or IDE:
   ```bash
   python number_guessing_game.py
   ```

## Gameplay Instructions
1. Run the game, and the program will generate a number between 1 and 100.
2. Enter your guesses in the terminal.
3. The program will tell you if your guess is too high, too low, or correct.
4. Type `exit` to quit the game at any time.

## Example
```
=== Welcome to the Number Guessing Game! ===
I have selected a number between 1 and 100.
Can you guess what it is?
Type 'exit' anytime to quit the game.
=============================================
Enter your guess: 50
Too high! Try a lower number.
Enter your guess: 25
Too low! Try a higher number.
Enter your guess: 35
Congratulations! You guessed the number 35 in 3 attempts.
Thanks for playing!
```

## Known Issues
- No advanced input validation beyond checking for integers.
- Players must restart the game to play again.

## Future Enhancements
- Add a difficulty level with adjustable range.
- Include a leaderboard to track high scores.

## License
This project is open-source and licensed under the MIT License.

---

### Author
Developed by [Your Name]. Suggestions and contributions are welcome!
