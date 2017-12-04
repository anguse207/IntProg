import math
from graphics import *

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    #centre = Point(150,150) 
    win = GraphWin("Brown Eye",300,300)    
    drawCircle(win, centre, 60, "white")
    drawCircle(win, centre, 30, "brown")
    drawCircle(win, centre, 15, "black")
    # Add your code here

# For exercise 5
def drawBrownEye(win, centre, radius):
    pass
    # Remove pass and add your code here

def circumferenceOfCircle(radius):    
    return math.pi * radius * 2

def circleInfo():
    radius = eval(input("Enter a radius > > "))
    print("Circumference = {0:0.3f} and the area = {1:0.3f}".format(circumferenceOfCircle(radius),areaOfCircle(radius)))


def drawBlockOfStars(x,y):
    for i in range(y):
        print("*" * x)


def drawLetterE():
    drawBlockOfStars(8,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(5,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(8,2)

def drawBlocks(z1,x1,z2,x2,y):
    for i in range(y):
        print(" " * z1 + "*" * x1 + " " * z2 + "*" * x2)
    
def drawLetterA():
    drawBlocks(1,8,0,0,2)
    drawBlocks(0,2,6,2,2)
    drawBlocks(0,10,0,0,2)
    drawBlocks(0,2,6,2,3)

def drawFourBrownEyes():
    for i in range(3):
        p1 = win.getMouse()
        centre = Point(p1.getX(),p1.getY())
        drawBrownEyeInCentre(centre)
        
        
    

    

drawFourBrownEyes()
