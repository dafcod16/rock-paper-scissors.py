import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    print("")
    userInput = input("Enter Rock, Paper, or Scissors to begin (or press 'q' to quit): ").lower()
    if userInput == "q":
        break
    if userInput not in options:
        continue

    randomNumber = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computerPick = options[randomNumber]
    print("The computer picked:" , computerPick)
    
    if userInput == "rock" and computerPick == "scissors":
        print("You won!")
        userWins += 1
    elif userInput == "paper" and computerPick == "rock":
        print("You won!")
        userWins += 1
    elif userInput == "scissors" and computerPick == "paper":
        print("You won!")
        userWins += 1
    elif userInput == computerPick:
        print("You tied!")
    else:
        print("You lost!")
        computerWins += 1


print("")
print("Thanks for playing!")
print("You won" , userWins , "games and the computer won" , computerWins , "games")

        
