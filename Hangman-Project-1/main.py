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
    hangman.penup()
    hangman.setposition(165, 210)
    hangman.pendown()
    hangman.fd(100)

def hangmanLegs():
    # Hangman legs
    hangman.right(45)
    hangman.fd(30)
    hangman.penup()
    hangman.setposition(165, 110)
    hangman.pendown()
    hangman.left(95)
    hangman.fd(30)

def hangmanHands():
    # Hangman hands
    hangman.penup()
    hangman.setposition(165, 185)
    hangman.pendown()
    hangman.right(95)
    hangman.fd(30)
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
    print(musicDict)
    print(musicDict.values())
    question = random.choice(list(musicDict.keys()))
    print(question)
    astrisk = '*' * len(musicDict[question])
    print(astrisk)
    for i in range(6):
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

        else:
            chanceCounter = i + 1
            print("-> you have used {} chance/s <-".format(chanceCounter))
            print("-> you have now {} chances left".format(constant - chanceCounter))


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
    hangmanStand()
    chooseField("Music")
    hangmanHead()
    hangmanLegs()
    hangmanHands()
    turtle.done()
