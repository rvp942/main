import random


def main():
    print("=== Welcome to the Number Guessing Game! ===")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")
    print("Type 'exit' anytime to quit the game.")
    print("=============================================")

    # Генериране на случайно число
    target_number = random.randint(1, 100)
    attempts = 0  # Брой опити на потребителя

    while True:
        user_input = input("Enter your guess: ")

        # Позволяване на потребителя да излезе от играта
        if user_input.lower() == "exit":
            print(f"The number was {target_number}. Better luck next time!")
            break

        # Проверка за валидност на въведеното число
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        # Увеличаване на броя на опитите
        attempts += 1

        # Проверка на предположението
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()