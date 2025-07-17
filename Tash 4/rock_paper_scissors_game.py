import random

def get_user_choice():
    print("\n Choose one: rock, paper, scissors")
    choice = input("Your Choice:").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, scissors")
        choice = input("Your Choice:").lower()
    return choice 

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif(user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"


def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n---- Round{round_number} ----")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Your Chice:{user_choice}")
        print(f"Computer Choice:{computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            print("You win this round.")
            user_score += 1
        elif result == "lose":
            print("You lost this round")
            computer_score += 1
        else:
            print("It's a tie")

        print(f"Score -> You:{user_score} | Computer:{computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Please answer with 'yes' or 'no': ").lower()

        if play_again == "no":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game() 
 
