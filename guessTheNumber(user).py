import random
def guess(x,y):
    number = random.randint(x, y)
    guess = int(input("Guess a number between x and y: "))
    while guess != number:
        if guess < number:
            print("Too low")
            guess = int(input("Guess again: "))
        elif guess > number:
            print("Too high")
            guess = int(input("Guess again: "))
    print("You guessed it!")
print("Welcome to Guess The Number Game")
fisrtNum = int(input("Enter the minimum limit: "))
lastNum = int(input("Enter the maximum limit: "))
while (fisrtNum > lastNum):
    print("Error number! Please type again: ")
    fisrtNum = int(input("Enter the minimum limit: "))
    lastNum = int(input("Enter the maximum limit: "))
guess(fisrtNum,lastNum)
