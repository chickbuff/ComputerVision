import random
from typing_extensions import Self

def get_computer_choice():
    game_words = ["rock", "paper", "scissors"]
    computer_choice  = random.choice(game_words)
    return computer_choice

    
def get_user_choice():
    while True:
        user_choice = input(" Please enter an option - Rock, Paper or Scissors: ")
        user_choice = user_choice.lower()
        if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
            return user_choice
        else:
            print(" Sorry, you must enter 'Rock', 'Paper' or 'Scissors' to play this game!")
        break

def get_winner(computer_choice, user_choice):
    if user_choice != computer_choice:
        if (user_choice == "rock" and computer_choice =="scissors") or (user_choice == "paper" and computer_choice =="rock") or (user_choice == "scissors" and computer_choice =="paper"):
            winner = "You"
            print(f" Congrats, {winner} win!")
        elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice =="scissors") or (user_choice == "scissors" and computer_choice =="rock"):
            winner = "Computer"
            print(f" {winner} wins! You Lose!")
    else:
        winner = "Tie"
        print(f" It's a {winner}!!!")
        return winner
    
def play():
    while True:
        result_comp = get_computer_choice()
        result_user = get_user_choice()
        final_winner = get_winner(result_comp, result_user)
        

play()
