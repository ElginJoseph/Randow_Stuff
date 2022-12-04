import random

user_action = input("Enter a choice (rock, paper or scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a draw")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rocks smashes scissors! You Win!")
    else:
        print("Paper covers rock! You Lose!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You Lose!")
    else:
        print("Scissors cut paper! You Lose!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You Win!")
    else:
        print("Rock samshes paper! You Lose!")
        
