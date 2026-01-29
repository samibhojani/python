import random

# used tuple because tuple is a read only, can't be modified with append or remove.
# choices = (ROCK, PAPER, SCISSOR)
# addding a dictionary to map keys with emojis. ie. r -> rock, s -> scissor, p -> paper
# emojis = {"r": "rock", "s": "scissors", "p": "paper"}

userName = input("Your Name:").capitalize()
ROCK = "r"
SCISSOR = "s"
PAPER = "p"
emojis = {ROCK: "Rock", SCISSOR: "Scissors", PAPER: "Paper"}
choices = tuple(emojis.keys())


def getUserChoice():
    while True:
        userChoice = input(
            "Rock, Paper, Scissors ? make your choice: r/p/s: ").lower()
        if userChoice in choices:
            return userChoice
        else:
            print("invalid input")

# getUserChoice function ends here


def displayUserAndMachineChoices(userChoice, machineChoice):

    print(f"You chose: {emojis[userChoice]} ")
    print(f"Computer chose: {emojis[machineChoice]}")


# Display choices function ends here

def DetermineWinsAndLoses(userChoice, machineChoice):

    if userChoice == machineChoice:
        print("It's a Tie.")
    elif (
        (userChoice == ROCK and machineChoice == SCISSOR) or
        (userChoice == SCISSOR and machineChoice == PAPER) or
            (userChoice == PAPER and machineChoice == ROCK)):

        print(f"{userName} you win!")
    else:
        print(f"{userName} you lose!")

    # DetermineWinsAndLoses function ends here


def playGame():
    while True:
        userChoice = getUserChoice()
        machineChoice = random.choice(choices)

        displayUserAndMachineChoices(userChoice, machineChoice)

        DetermineWinsAndLoses(userChoice, machineChoice)

        playAgain = input("continue to play ? y/n:").lower()
        if playAgain == "n":
            print(f"Goodbye! {userName}")
            break


playGame()
