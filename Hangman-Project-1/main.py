import turtle
import random

constant = 6

def hangmanStand():
    # Hangman stand
    hangman.forward(130)
    hangman.setposition(65, 0)
    hangman.left(90)
    hangman.forward(350)
    hangman.right(90)
    hangman.forward(100)
    hangman.right(90)
    hangman.forward(100)

def hangmanHead():
    # Hangman head
    hangman.penup()
    hangman.setposition(145,230)
    hangman.pendown()
    hangman.circle(20)

def hangmanBody():
    hangman.penup()
    hangman.setposition(165, 210)
    hangman.pendown()
    hangman.fd(100)

def hangmanLeftLeg():
    # Hangman left leg
    hangman.right(45)
    hangman.fd(30)

def hangmanRightLeg():
    hangman.penup()
    hangman.setposition(165, 110)
    hangman.pendown()
    hangman.left(95)
    hangman.fd(30)

def hangmanLeftHand():
    # Hangman hands
    hangman.penup()
    hangman.setposition(165, 185)
    hangman.pendown()
    hangman.right(95)
    hangman.fd(30)
def hangmanRightHand():
    hangman.penup()
    hangman.setposition(165,185)
    hangman.pendown()
    hangman.left(95)
    hangman.fd(30)

def chooseField(fieldName):
    print("Welcome to {} section".format(fieldName))
    musicDict = {}
    file1 = open('music_Questions.txt', 'r')
    lines = file1.read().split(':')
    for i in range(0, len(lines) - 1, 2):
        musicDict[lines[i]] = lines[i+1]
    # print(musicDict)
    # print(musicDict.values())
    question = random.choice(list(musicDict.keys()))
    print(question)
    astrisk = '*' * len(musicDict[question])
    print(astrisk)
    chanceCounter = 0
    numberOfTimesPlayed = 0
    response = False
    start = True
    while start:
        if response:
            chanceCounter = 0
            print("Welcome again")
            hangman = turtle.Turtle()
            turtle.Screen().reset()
            turtle.bgcolor("green")
            hangman.pensize(3)
            hangman.hideturtle()
            turtle.title("Welcome to Bishalii's Hangman game")
            hangmanStand()
            question = random.choice(list(musicDict.keys()))
            print(question)
            astrisk = '*' * len(musicDict[question])
            print(astrisk)

        name = input("Enter your guessing character: ")

        if name in musicDict[question]:
            indices = []
            findingChar = -1
            while True:
                findingChar = musicDict[question].find(name, findingChar + 1)
                if findingChar == -1:
                    break
                else:
                    indices.append(findingChar)
            astrisk = list(astrisk)
            for index in indices:
                astrisk[index] = name
            astrisk = "".join(astrisk)
            print(astrisk)
            response = False

        else:
            chanceCounter += 1
            print("-> you have used {} chance/s <-".format(chanceCounter))
            print("-> you have now {} chance/s left <-".format(constant - chanceCounter))
            if chanceCounter == 1:
                hangmanHead()
                response = False
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
                turtle.write("Game Over")
                userInput = input("Do you want to play again(y/n)?: ")
                if userInput == 'y':
                    numberOfTimesPlayed += 1
                    response = True
                else:
                    numberOfTimesPlayed += 1
                    print("You played {} time/s")
                    print("Good bye till next time >>> ")
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
    turtle.done()
