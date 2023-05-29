def gender(gender):
    if(gender == "Male"):
        return "he"
    elif(gender == "Female"):
        return "she"
print("Enter your age: ")
age=int(input("Age: "))
if(age < 18):
    print("You are not old enough to play this game")
else:
    print("Welcomt to the game")
    print(f'Design your character:\n')
    name=input("Name:")
    age=input("Age:")
    sex=input("Gender:")
    while (sex != "Male" or sex != "Female"):
        print("Invalid gender. Do you want to retype? (Y) for yes or (N) for no")
        sexChoice = str(input())
        if(sexChoice == "N"):
            break
        elif(sexChoice == "Y"):
           sex=input("Gender:") 
    weapon=input("Weapon:")
    monster=input("Monster:")
    v1=input("Verb:")
    v2=input("Verb:")
    v3=input("Verb:")
    monsterColor=input("Monster Color:")
    monsterState=input("Monster State:")
    bounty=input("Reward for defeating monster:")
    while(name is None or age is None or weapon is None or monster is None or v1 is None or v2 is None or v3 is None or monsterColor is None or monsterState is None):
        if(name is None):
           name=input("Name:")
        elif(age is None):     
              age=input("Age:")
        elif(weapon is None):
                weapon=input("Weapon:")
        elif(monster is None):
                monster=input("Monster:")
        elif(v1 is None):
                v1=input("Verb:")
        elif(v2 is None):
                v2=input("Verb:")
        elif(v3 is None):
                v3=input("Verb:")
        elif(monsterColor is None):
                monsterColor=input("Monster Color:")
        elif(monsterState is None):
                monsterState=input("Monster State:")
    print(f'Your character is {name}, has survived for {age} years. Today {gender(sex)} will go to defeat {monsterColor} {monsterState} {monster} with the {weapon}. After {v1}ing, {v2}ing, {v3}ing, the monster start to be exhausted and then died. The warrior come back to receive {bounty} for defeating the monster')
