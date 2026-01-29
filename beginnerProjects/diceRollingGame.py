import random

while True:
    userChoice = input("Roll the dice ? y/n:").lower()
    if userChoice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"you rolled a {dice1} and a {dice2}")
    elif userChoice == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input")
