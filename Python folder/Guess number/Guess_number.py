import random  # Import the random module to generate random numbers

def main():
    # Print game instructions
    print("=== Welcome to the Number Guessing Game! ===")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")
    print("Type 'exit' anytime to quit the game.")
    print("=============================================")

    target_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the number of attempts

    while True:  # Main game loop
        user_input = input("Enter your guess: ")  # Get user input

        # Allow the user to exit the game
        if user_input.lower() == "exit":
            print(f"The number was {target_number}. Better luck next time!")
            break  # Exit the loop

        # Validate if the input is a number
        try:
            guess = int(user_input)  # Try converting the input to an integer
        except ValueError:  # If conversion fails, handle the error
            print("Invalid input. Please enter a number between 1 and 100.")
            continue  # Skip to the next iteration of the loop

        attempts += 1  # Increment the attempt counter

        # Provide feedback on the guess
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:  # Correct guess
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break  # Exit the loop

    print("Thanks for playing!")  # End message when the game is over

if __name__ == "__main__":
    main()  # Run the game
