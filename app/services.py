import random
import time

def display_rules():
    print("Welcome To Rock Paper Scissors!")
    print("Rules:")
    print("1: Rock beats Scissors.")
    print("2: Scissors beats Paper.")
    print("3: Paper beats Rock.")
    print("4: First to 3 points wins the game!")
    print("-" * 40)

def get_user_choice():
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    while True:
        print("\nChoose your move:")
        print("1: Rock ")
        print("2: Paper ")
        print("3: Scissors ")
        user_input = input("Enter the number of your choice (1-3): ")
        if user_input in choices:
            return choices[user_input]
        print("Invalid Selection, try again!")

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

def play_round():
    user_choice = get_user_choice() 
    computer_choice = get_computer_choice() 

    print(f"\nYou Chose: {user_choice}")
    time.sleep(0.5)
    print(f"Computer Chose: {computer_choice}")
    time.sleep(0.5)

    winner = determine_winner(user_choice, computer_choice)
    if winner == "Draw":
        print("It's a draw!")
    elif winner == "User":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner