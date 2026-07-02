import random
choices = ["rock", "paper", "scissors"]
user = input("Enter your choice (rock/paper/scissors):").lower()
computer = random.choice(choices)
print("Computer choice:", computer)
if user == computer:
    print("Tie")
elif user == "rock" and computer == "scissors":
    print("User Wins")
elif user == "paper" and computer == "rock":
    print("User Wins")
elif user == "scissors" and computer == "paper":
    print("User Wins")
else:
    print("Computer Wins")