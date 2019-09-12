import turtle
import random

constant = 6

# Hangman stand
def hangmanStand():
    hangman.forward(130)
    hangman.setposition(65, 0)
    hangman.left(90)
    hangman.forward(350)
    hangman.right(90)
    hangman.forward(100)
    hangman.right(90)
    hangman.forward(100)


def hangmanHead():  # Hangman head
    hangman.penup()
    hangman.setposition(145,230)
    hangman.pendown()
    hangman.circle(20)


def hangmanBody(): # Hangman body
    hangman.penup()
    hangman.setposition(165, 210)
    hangman.pendown()
    hangman.fd(100)


def hangmanLeftLeg():  # Hangman left leg
    hangman.right(45)
    hangman.fd(30)


def hangmanRightLeg():  # Hangman right leg
    hangman.penup()
    hangman.setposition(165, 110)
    hangman.pendown()
    hangman.left(95)
    hangman.fd(30)


def hangmanLeftHand():  # Hangman left hand
    hangman.penup()
    hangman.setposition(165, 185)
    hangman.pendown()
    hangman.right(95)
    hangman.fd(30)


def hangmanRightHand():  # Hangman right hand
    hangman.penup()
    hangman.setposition(165, 185)
    hangman.pendown()
    hangman.left(95)
    hangman.fd(30)


def chooseField(fieldName):
    print("Welcome to {} section".format(fieldName))
    musicDict = {}  # dictionary to keep key value pair of questions and answers
    file1 = open('music_Questions.txt', 'r')
    lines = file1.read().split(':')
    print(len(lines))
    for i in range(0, len(lines) - 1, 2):
        musicDict[lines[i]] = lines[i+1]  # assigning right key with right value after splitting the text
    question = random.choice(list(musicDict.keys()))
    print(question)  # displaying random questions to the player
    asterisk = '*' * len(musicDict[question])
    print(asterisk)
    chanceCounter = 0  # Keeps track of number of chances player has
    numberOfTimesPlayed = 0  # Keeps track of number of times player has played
    response = False  # helper variable for new turtle window
    start = True

    while start:
        if response: # Executes only when player wants to play the game again
            chanceCounter = 0
            print('=' * 20)
            print("Welcome again")
            print('=' * 20)
            turtle.Screen().reset()
            turtle.title("Welcome to Bishal's Hangman game")
            hangman.pensize(3)
            hangman.hideturtle()
            hangmanStand()
            question = random.choice(list(musicDict.keys()))
            print(question)
            asterisk = '*' * len(musicDict[question])
            print(asterisk)

        character = input("Enter your guessing character: ")

        if character in musicDict[question]:
            indices = []  # finding the index of character/ repeated character and storing into it.
            findingChar = -1
            while True:
                findingChar = musicDict[question].find(character, findingChar + 1)  # to find the index of char
                if findingChar == -1:
                    break
                else:
                    indices.append(findingChar)
            asterisk = list(asterisk)
            for index in indices:
                asterisk[index] = character  # replace the '*' character with the appropriate letter if found
            print('=' * 20)
            asterisk = "".join(asterisk)  # joining the list with no spaces to make it look like a word.
            print(asterisk)
            print('=' * 20)
            response = False

        else:
            chanceCounter += 1
            print("-> you have used {} chance/s <-".format(chanceCounter))
            print("-> you have now {} chance/s left <-".format(constant - chanceCounter))
            if chanceCounter == 1:
                hangmanHead()
                response = False  # to prevent entering into the block of line 77 again and again.
            elif chanceCounter == 2:
                hangmanBody()
                response = False
            elif chanceCounter == 3:
                hangmanLeftLeg()
                response = False
            elif chanceCounter == 4:
                hangmanRightLeg()
                response = False
            elif chanceCounter == 5:
                hangmanLeftHand()
                response = False
            else:
                hangmanRightHand()
                turtle.write("Game Over", font=("Arial", 14, "normal"))
                userInput = input("Do you want to play again(y/n)?: ")
                if userInput == 'y':
                    numberOfTimesPlayed += 1
                    response = True
                else:
                    numberOfTimesPlayed += 1
                    print('=' * 35)
                    print("You played {} time/s".format(numberOfTimesPlayed))
                    print("Good bye till next time >>> ")
                    print('=' * 35)
                    turtle.Screen().bye()
                    break


if __name__ == '__main__':
    hangman = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("green")
    hangman.pensize(3)
    hangman.hideturtle()
    turtle.title("Welcome to Bishal's Hangman game")
    print('=' * 35)
    print("Welcome to Bishal's hangman game")
    print('=' * 35)
    print("""
    Game Rules:
    1) You should guess the name within six tries.
    2) You should save the cartoon character to be hanged.
    """)

    print('=' * 100)
    hangmanStand()
    chooseField("Music")
