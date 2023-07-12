'''Judith plays rock paper Scissors With Computer
    Rock, paper, Scissors'''

from random import randint

moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0, 2)]
    player = input("Rock, Paper, Scissors(Enter 'end game' to exit)").lower()

    if player == 'end game':
        print("Game Over")
        break

    elif player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose", computer, "beats", player)
        else:
            print("You won")
    elif player == "paper":
        if computer =="scissors":
            print("You lose", computer, "beats", player)
        else:
            print("You won")
    elif player =="scissors":
        if computer =="rock":
            print("You lose", computer, "beats", player)
        else:
            print("You won")
    else:
        print("Check your spelling")























    