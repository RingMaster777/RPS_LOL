import os
import random
import sys


def game(a, b):

    if(a == 1):
        a = 'r'
    elif(a == 2):
        a = 'p'
    elif(a == 3):
        a = 's'

    # print(f("comp: {a}"))
    # print(f("you: {b}"))

    if(a == b):
        return False
    elif(a == 'r'):
        if(b == 'p'):
            return True
        elif(b == 's'):
            return False
    elif(a == 'p'):
        if(b == 'r'):
            return False
        elif(b == 's'):
            return True
    elif(a == 's'):
        if(b == 'r'):
            return True
        elif(b == 'p'):
            return False


def runchoice():
    choice = input("Do you wanna Try again (y/n): ")
    if(choice == 'y'):
        player = input("Rock(r), Paper(p) or Scissor(s) : ")
        randomNumber = random.randint(1, 3)
        if(game(randomNumber, player)):
            print("congratulations")
            runchoice()
        else:
            print("sorry")
            runchoice()
    else:
        sys.exit()


player = input("Rock(r), Paper(p) or Scissor(s) : ")
randomNumber = random.randint(1, 3)
if(game(randomNumber, player)):
    print("congratulations")
    runchoice()
else:
    print("sorry")
    runchoice()
