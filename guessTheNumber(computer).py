import random
def guess(x,y,number):
    choice = random.randint(x, y)
    while choice != number:
        print("The computer guessed: ", choice)
        appraise = str(input("Is it too high or too low? (H) for high or (L) for low: "))
        if appraise == "H":
            choice = random.randint(x, choice)
        elif appraise == "L":
            choice = random.randint(choice, y)
    print("The computer guessed: ", choice)
    print("You guessed it!")
print("Welcome to Guess The Number Game")
fisrtNum = int(input("Enter the minimum limit: "))
lastNum = int(input("Enter the maximum limit: "))
while (fisrtNum > lastNum):
    print("Error number! Please type again: ")
    fisrtNum = int(input("Enter the minimum limit: "))
    lastNum = int(input("Enter the maximum limit: "))
number = int(input("Enter a number between x and y: "))
guess(fisrtNum,lastNum,number)