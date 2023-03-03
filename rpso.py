import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):\n").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Its a tie"
    elif player == "rock" :
        if computer == "scissors":
            return "rock smashes scissors, you win"
        else:
            return "paper covers rock, you lose"
    elif player == "paper" :
        if computer == "scissors":
            return " scissors cuts paper, you lose"
        else:
            return "paper covers rock, you win"
    elif player == "scissors" :
        if computer == "paper":
            return "scissors cuts paper, you win"
        else:
            return "rock smashes, you lose"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)