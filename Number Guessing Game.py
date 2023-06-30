import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("WELCOME TO JUDITH NUMBER GUESSING GAME")
    print("I have pick a number between 1 and 100, can you guess?")

    while True:
        guess = int(input("Take a Guess: "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Please start a new guess:Select from 1 - 100, THANK YOU!")
            continue

        if guess < secret_number:
            print("Too low,Take a new guess")
        elif guess > secret_number:
            print("Too High, Take a new guess")
        else:
            print(f"Congratulation you guess the number in {attempts} attempts. ")
            print("Start a New game: CONTINUE GUESSING: BRAVO!!!")

guess_number()
