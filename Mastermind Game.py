import random

def get_valid_guess():
    """Get a valid multi-digit guess from the player."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 10 <= guess <= 20:  
                return guess
            else:
                print("Please enter a valid 2-digit number.")
        except ValueError:
            print("Please enter a number between 10-20.")

def compare_numbers(secret, guess):
    """Compare the secret number with the guessed number and return the matching digits."""
    return sum([1 for s, g in zip(str(secret), str(guess)) if s == g])

def play_game():
    print("Welcome to the Mastermind game!")

    
    secret_number_p1 = random.randint(10, 20)    
    print("Player 1 has set the secret number.")

   
    attempts_p2 = 0
    while True:
        guess_p2 = get_valid_guess()
        attempts_p2 += 1

        if guess_p2 == secret_number_p1:
            print(f"Congratulations! Player 2 guessed the number in {attempts_p2} attempts.")
            print("Player 2 is crowned Mastermind!")
            break
        else:
            matching_digits = compare_numbers(secret_number_p1, guess_p2)
            print(f"Incorrect guess. Player 2 got {matching_digits} digit(s) correct. Try again.")

  
    secret_number_p2 = random.randint(10, 20)
    print("Player 2 has set the secret number.")

   
    attempts_p1 = 0
    while True:
        guess_p1 = get_valid_guess()
        attempts_p1 += 1

        if guess_p1 == secret_number_p2:
            print(f"Congratulations! Player 1 guessed the number in {attempts_p1} attempts.")
            print("Player 1 is crowned Mastermind!")
            break
        else:
            matching_digits = compare_numbers(secret_number_p2, guess_p1)
            print(f"Incorrect guess. Player 1 got {matching_digits} digit(s) correct. Try again.")

   
    if attempts_p1 < attempts_p2:
        print("Player 1 wins! Player 1 is the ultimate Mastermind.")
    elif attempts_p2 < attempts_p1:
        print("Player 2 wins! Player 2 is the ultimate Mastermind.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
