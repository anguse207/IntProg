#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

from graphics import *
import time

# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:        
        time.sleep(5)
        amber.setFill("Yellow")
        amber.undraw()
        amber.draw(win)
        time.sleep(1.5)
        red.setFill("black")
        red.undraw()
        red.draw(win)        
        amber.setFill("Black")
        amber.undraw()
        amber.draw(win)
        green.setFill("Green")
        green.undraw()
        green.draw(win)
        time.sleep(5)
        amber.setFill("Yellow")
        amber.undraw()
        amber.draw(win)
        green.setFill("Black")
        green.undraw()
        green.draw(win)
        time.sleep(1.5)
        amber.setFill("Black")
        amber.undraw()
        amber.draw(win)        
        red.setFill("Red")
        red.undraw()
        red.draw(win)
        time.sleep(5)

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def getName():
    validInput=False
    while validInput == False:
        name=input("Enter your first name > > ")
        if name.isalpha():
            validInput=True
            return name
        else:
            print("invalid input")

def gradeCoursework():
    validInput = False
    while validInput == False:
        mark = eval(input("Enter the mark > > "))
        if mark <= 20 and mark >= 0:
            print("the grade is ...")#code from pract06
            #validInput = True
        else:
            print("Invalid input")
            

def orderPrice():
    orderFinished = False
    totalCost = 0
    while orderFinished == False:
        unitPrice =  eval(input("What is the unit price? > > "))
        unitQty =  eval(input("What is the unit quantity? > > "))
        totalCost += (unitPrice * unitQty)        
        moreItems = input("Do you need to add more products to the order? Y/N> > ")
        if moreItems =="N":
            orderFinished = True

    print("The total cost is $",totalCost)



orderPrice()
        








































    
