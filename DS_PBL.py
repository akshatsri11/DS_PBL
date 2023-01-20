import random

scoreboard = {"wins": 0, "losses": 0, "ties": 0}

def game():
    # Get the player's choice
    player_choice = input("Rock, paper, or scissors? ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        return
   
    # Get the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("The computer chose " + computer_choice + ".")
    
    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
        scoreboard["ties"] += 1
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        scoreboard["wins"] += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        scoreboard["wins"] += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        scoreboard["wins"] += 1
    else:
        print("You lose.")
        scoreboard["losses"] += 1
        
    # Print the scoreboard
    print("Wins: " + str(scoreboard["wins"]))
    print("Losses: " + str(scoreboard["losses"]))
    print("Ties: " + str(scoreboard["ties"]))

while True:
    game()