def compare(computerChoice, userChoice):
    if(computerChoice == userChoice):
        return "Tie"
    elif(computerChoice == "rock" and userChoice == "paper"):
        return "User Wins"
    elif(computerChoice == "rock" and userChoice == "scissors"):
        return "Computer Wins"
    elif(computerChoice == "paper" and userChoice == "rock"):
        return "Computer Wins"
    elif(computerChoice == "paper" and userChoice == "scissors"):
        return "User Wins"
    elif(computerChoice == "scissors" and userChoice == "rock"):
        return "User Wins"
    elif(computerChoice == "scissors" and userChoice == "paper"):
        return "Computer Wins"
    else:
        return "Wrong choice!"
def RPSGame():
    import random
    print("Welcome to Rock, Paper, Scissors Game")
    print("Please enter your choice: ")
    userChoice = input("rock, paper or scissors? ")
    computerChoice = random.choice(["rock", "paper", "scissors"])
    print("Computer choice: " + computerChoice)
    print(compare(computerChoice, userChoice))
RPSGame()
