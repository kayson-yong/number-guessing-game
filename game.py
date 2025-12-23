import random

secret_number = random.randint(1, 15)
player_guess = 0

while player_guess != secret_number:
    print("Guess a number between 1 and 15 inclusive:")
    player_guess = int(input())

    if player_guess < secret_number:
        print("Too low! Try again!")
    elif player_guess > secret_number:
        print("Too high! Try again!")
    else:
        print("Correct! You guessed the number.")
