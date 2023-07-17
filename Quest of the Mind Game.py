"""Judith Quest of the mind game, is a number guessing Challenge, Which involves a
 player to guess 10 number between 1 - 10"""
from random import randint
while True:
    score = 5

    for guess_number in range(10):
        random_num = randint(1, 10)
        guess = input("Take a guess or 'exit' to quit: ")

        if guess == 'exit':
            print("Successfully Exited")
            break

        try:
            guess_number = int(guess)
            if guess_number == random_num:
                print("Congrats! You guessed correctly.")
                score += 10
            elif guess_number < 1 or guess_number > 10:
                print("Error: Enter a number within the range 1-10.")
            else:
                print("Sorry, wrong guess.")
                score -= 1
        except ValueError:
            print("Invalid input. Enter a number or 'exit' to quit.")

    print(f"Game score: {score}")
    print("Game Over")
