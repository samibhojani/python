import random

machinesNumber = random.randint(1, 100)
while True:
    try:
        usersGuessedNumber = int(input("Guess the number between 1 and 100: "))

        if usersGuessedNumber != int():
            print("Invalid input! please enter a number")
        if usersGuessedNumber < machinesNumber:
            print("Too Low!")
        elif usersGuessedNumber > machinesNumber:
            print("Too High!")
        elif usersGuessedNumber == machinesNumber:
            print("You won! you guessed the number!")
            break
    except ValueError:
        print("Invalid input! Please add a valid number")
