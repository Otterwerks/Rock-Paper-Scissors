#Rock Paper Scissors
import random

choices = ["Rock", "Paper", "Scissors", "Quit", "Score"]
player1 = 0
player2 = 0

def opponent():
    choice = choices[random.randint(0,2)]
    return choice

def victory():
    print("You Win!\n")
    global player1
    player1 = player1 + 1

def defeat():
    print("You Lose!\n")
    global player2
    player2 = player2 + 1

def tie():
    print("Try again...\n")

print("Welcome to Rock Paper Scissors!")
print("To play the game: type in Rock, Paper, or Scissors. To view your score type Score. To exit the game type Quit.")
name = input("What is your name? ")

while True:
    print("\nRo Sham Bo...\n")
    userInput = str(input())
    npc = opponent()

    if userInput not in choices:
        print("Choose either Rock, Paper, or Scissors")

    elif userInput == "Quit":
        print("Goodbye")
        break

    elif userInput == "Score":
        print("\n" + name + " Score: " + str(player1))
        print("Computer Score: " + str(player2))

    elif userInput == "Rock" or userInput =="Paper" or userInput == "Scissors":
        print("\nYour opponent plays " + npc)

        if userInput == "Rock":
            if npc == "Scissors":
                victory()
            elif npc == "Paper":
                defeat()
            elif npc == "Rock":
                tie()

        elif userInput == "Paper":
            if npc == "Rock":
                victory()
            elif npc == "Scissors":
                defeat()
            elif npc == "Paper":
                tie()

        elif userInput == "Scissors":
            if npc == "Paper":
                victory()
            elif npc == "Rock":
                defeat()
            elif npc == "Scissors":
                tie()


