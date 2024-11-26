from services import display_rules, get_computer_choice, get_user_choice, determine_winner, play_round

def main():
    display_rules()
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while user_score < 3 and computer_score < 3:

        print(f"\n--- Round {rounds_played +1} ---")

        result = play_round()

        rounds_played+=1

        if result == "User":
            user_score+=1

        elif result == "Computer":
            computer_score+=1

        print(f"Current Scores: You {user_score} - {computer_score} Computer")
        print("-"*40)

    if user_score == 3:
        print("Congratulations! You Won the Game!")
    
    else:
        print("AI took your job, GG")

    while True:
        play_again_choice = input("Do you want to play again? y/n: ")
        if play_again_choice == 'y':
            return main()
        elif play_again_choice == 'n':
            return 0
        else:
            print("You made a typo, please try again!")

if __name__ == "__main__":
    main()