import turtle
import random

def hangmanStand():
    # Hangman stand
    hangman.forward(130)
    hangman.setposition(65,0)
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
    lines = file1.readline().split(':')
    while lines:
        musicDict[lines[0]] = lines[1]
        lines = file1.readline().split(':')
    print(musicDict)
    question = random.choice(list(musicDict.keys()))
    print(question)
    print(musicDict[question])
    name = input("Enter the winner name: ")
    if musicDict[question].strip('\n') == name:
        print("Correct")
    else:
        print("Incorrect")



if __name__ == '__main__':

    hangman = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("green")
    hangman.pensize(3)
    hangman.hideturtle()
    turtle.title("Welcome to Bishal's Hangman game")
    print("Welcome to Bishal's hangman game")
    print("""
    Game Rules:
    1) You should guess the name within six tries.
    2) You should save the cartoon character to be hanged.
    """)
    # hangmanStand()
    chooseField("Music")
    # hangmanHead()
    # hangmanLegs()
    # hangmanHands()
    turtle.done()
