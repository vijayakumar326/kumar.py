import random

def welcome_message():
    """Print a welcome message to the user."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

def get_user_guess():
    """Prompt the user to enter a guess and handle invalid input."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    """Main game logic for the number guessing game."""
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = get_user_guess()
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
def main():
    """Start the game and manage the overall flow."""
    welcome_message()
    play_game()
    
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game()
        elif play_again == 'n':
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
