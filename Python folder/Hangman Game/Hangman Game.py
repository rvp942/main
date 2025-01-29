import random


# Function to choose a random word from a predefined list
def choose_word():
    words = ["python", "programming", "developer", "hangman", "challenge"]  # List of possible words
    return random.choice(words)  # Select a random word from the list


# Function to display the word with guessed letters and hide the others
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Main function for the Hangman game
def hangman():
    word = choose_word()  # Select a word
    guessed_letters = set()  # Store guessed letters
    attempts = 6  # Number of attempts the player has

    print("Welcome to Hangman!")  # Welcome message

    while attempts > 0:  # Game loop
        print(f"\nWord: {display_word(word, guessed_letters)}")  # Display current progress
        guess = input("Guess a letter: ").lower()  # Take user input and convert to lowercase

        # Validate input: must be a single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)  # Add letter to guessed set

        if guess not in word:
            attempts -= 1  # Decrease attempts if the letter is incorrect
            print(f"Wrong guess! Attempts left: {attempts}")
        else:
            print("Good guess!")

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return  # End the game if the word is fully guessed

    print(f"Game over! The word was: {word}")  # Display game over message


# Run the game if the script is executed directly
if __name__ == "__main__":
    hangman()