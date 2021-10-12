import random

#create variables that count the user and computer wins
userWins = 0
computerWins = 0

#create a list that consists of rock paper scissors
options = ["rock", "paper", "scissors"]

while True:
    #line break to create more readable output
    print("")
    #allow user to input their pick, .lower() to make it lowercase
    userInput = input("Enter Rock, Paper, or Scissors to begin (or press 'q' to quit): ").lower()
    if userInput == "q":
        break
    #if user does not enter one of the options, ask question again
    if userInput not in options:
        continue

    #create random number and assign it a value in options list
    randomNumber = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computerPick = options[randomNumber]
    print("The computer picked:" , computerPick)
    
    #create scenarios for wins, tie, and loss
    if userInput == "rock" and computerPick == "scissors":
        print("You won!")
        #adds to user wins
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
        #adds to computer wins
        computerWins += 1


#print off score after user exists program
print("")
print("Thanks for playing!")
print("You won" , userWins , "games and the computer won" , computerWins , "games")

        
