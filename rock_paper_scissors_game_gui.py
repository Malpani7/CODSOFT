import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "IT's a tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You Win"
    else:
        return " You Lose"

def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"Your Choice:{user_choice}")
    computer_choice_label.config(text=f"Computer Choice:{computer_choice}")
    result_label.config(text=f"Result:{result}")

    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score +=1

    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")        

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score -> You: 0 | Computer: 0")

# Main Window
    
root = tk.Tk()
root.title("Rock, Paper, Scissors")

user_score = 0
computer_score = 0

#Lables
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)


#Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

#Run The App
root.mainloop()
