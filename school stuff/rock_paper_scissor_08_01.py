import random

user_action = input("Enter a choice (rock, paper, scissor):")
possible_action = ["rock", "paper", "scissor"]
computer_action = random.choice(possible_action)
print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both Players selected {user_action}. It's a Tie!")

