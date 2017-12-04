#PRACTICAL WORKSHEET 4
from graphics import *

def personalGreeting():
    name = input("What is your name? > > ")
    print("Hello " + name + ", nice to see you!")
    
def formalName():
    fname = input("What is your first name? > > ")
    lname = input("What is your last name? > > ")
    print(fname[0] + ". " + lname)
    
def kilos2pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))

def generateEmail():
    fname = input("What is your first name? > > ")
    lname = input("What is your last name? > > ")
    year = str(input("Enter the year you started university > > "))
    print(lname.lower()[0:4] + "." + fname.lower()[0] + "." + year[2:4] + "@myport.ac.uk")

def gradeTest():
    grades = "FFFFCCBBAAA"
    marks = eval(input("How many marks? > > "))
    print(grades[marks])
    
def graphicsLetters():
    win = GraphWin("Graphics Letters",300,300)
    word = input("Enter a word > > ")
    for i in range(len(word)):
        p = win.getMouse()
        message = Text(Point(p.getX(),p.getY()), word[i])
        #message = Text.setSize(20)
        message.draw(win)
    
    win.getMouse()
    win.close()

def singASong():
    word = input("Enter the songs word > > ")
    lines = eval(input("How many lines? > > "))
    times = eval(input("How many repeats? > > "))
    for i in range(lines):
        print(word * times)
