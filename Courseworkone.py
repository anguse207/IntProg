#INTPROG COURSEWORK 1
# Angus Edmunds 855751

from graphics import *

def penultimate(win,startX,startY,colour):#this is used for printing the penultimate digit(5)
    for i in range(10):
        lineX = Line(Point(startX+(10*i),startY+ 1), Point(startX+100,startY+10+(i*10)))
        lineY = Line(Point(startX+(0), startY+10*i), Point(startX+10+(i*10),startY+100))
        lineX.setFill(colour)
        lineY.setFill(colour)
        lineX.draw(win)
        lineY.draw(win)

    border = Rectangle(Point(startX, startY), Point(startX + 100, startY + 100))
    border.setOutline(colour)
    border.draw(win)

def finalDigit(win,startX,startY,colour):#this is used for printing the final digit(1)
    for x in range(10):
        for i in range(7):
            #THIS BLOCK STOPS THE RECTANGLE LEAVING ITS 100X100 CELL
            x1=startX+(0+30*i)-10*x
            if x1 <= startX:
                x1=startX+1
            elif x1 >= (startX+99):
                x1=(startX+99)
            x2=startX+(20+30*i)-10*x
            if x2 <= startX:
                x2=startX
            elif x2 >= (startX+100):
                x2=(startX+100)

            y1 = startY + 0 + (10 * x)
            y2=startY+10+(10*x)
            rectangle1 = Rectangle(Point(x1,y1), Point(x2,y2))
            rectangle1.setFill(colour)
            rectangle1.draw(win)

    border = Rectangle(Point(startX,startY), Point(startX+100,startY+100))
    border.draw(win)

def validateInput(sizeInput,colour1,colour2,colour3):#this function is for validating input in gatherInput()
    sizePass=0
    #CHECK SIZE INPUT
    validSizes=[5,7,9,11]
    if sizeInput != "":
        if int(sizeInput) in validSizes:
            sizePass=1
        else:
            pass
    else:
        pass
    #CHECK COLOUR INPUT(S)
    colourPass=0
    validColours = ["red", "green", "blue" , "magenta", "cyan",
                    "orange", "brown", "pink"]
    colour1 = colour1.lower()
    colour2 = colour2.lower()
    colour3 = colour3.lower()
    if colour1 in validColours and colour2 in validColours and colour3 in validColours:
        if colour1==colour2 or colour1==colour3 or colour2==colour3:
            pass
        else:
            colourPass=1
    else:
        pass
    #return if valid
    if sizePass==1 and colourPass==1:
        return "valid"

def gatherInput(): #this function creates a new window and
    win=GraphWin("Choose Window Size & 3 Colours",450,250)
    message = Text(Point(225, 20), "Enter the desired window size and 3 colours!").draw(win)
    message = Text(Point(103, 55), "Window Size - (5,7,9,11)").draw(win)
    sizeInput = Entry(Point(30,75),2).draw(win)
    message = Text(Point(213, 100), "Colours-red,green,blue,magenta,cyan,orange,brown,pink").draw(win)
    c1 = Entry(Point(51, 120), 7).draw(win)
    c2 = Entry(Point(51, 160), 7).draw(win)
    c3 = Entry(Point(51, 200), 7).draw(win)
    doneButton = Rectangle(Point(350,175), Point(448,248)).draw(win)
    message = Text(Point(400, 212), "Done").draw(win)
    inputLoop=1
    while inputLoop==1:
        p = win.getMouse()
        if p.getX() > 270 and p.getY() > 130:
            if (validateInput(sizeInput.getText(),c1.getText(),c2.getText(),c3.getText())) =="valid":
                inputLoop=0
                win.close()
                return int(sizeInput.getText()),c1.getText(),c2.getText(),c3.getText()
            else:
                message = Text(Point(225, 220), "Invalid Input!").draw(win)

def blankSquare(win,x1,y1,x2,y2):#this function creates a blank square, used in main()
    rectangle = Rectangle(Point(x1, y1), Point(x1+100,y1+100))
    rectangle.setFill("white")
    rectangle.draw(win)
    rectangle = Rectangle(Point(x2, y2), Point(x2 + 100, y2 + 100))
    rectangle.setFill("white")
    rectangle.draw(win)

def createGrid(windowSize):#This function creates a list which details the way the grid is draw
    distanceToMiddle = windowSize // 2 #this gets the amount of cells from top/bottom to the centre line
    return (["f"] + ["P"] * (windowSize - 2) + ["f"]) * distanceToMiddle + \
                 ["f"] * (windowSize) + \
                 (["f"] + ["P"] * (windowSize - 2) + ["f"]) * distanceToMiddle

def main():
    windowSize,c1,c2,c3 = gatherInput()
    gridLayout=createGrid(windowSize)
    colours=[c1,c2,c3]*50 #create a list of colours to go through
    colourCount=0 #count the current number in the list of colours

    win=GraphWin("Coursework One",100*windowSize,100*windowSize)
    for y in range(windowSize):
        for i in range(windowSize):
            if gridLayout[(windowSize*y)+i]=="f":
                finalDigit(win, 0+(i*100), 0+(100*y), colours[colourCount])
            else:
                penultimate(win, 0+(i)*100, 0+(100*y), colours[colourCount])
            colourCount += 1

    #ADVANCED PROGRAM FEATURE
    while True:
        p1 = win.getMouse()
        swapX1 = int(p1.getX() // 100)
        swapY1 = int(p1.getY() // 100)
        swapIndex1 = swapX1 + (swapY1 * windowSize)

        p1 = win.getMouse()
        swapX2 = int(p1.getX() // 100)
        swapY2 = int(p1.getY() // 100)
        swapIndex2 = swapX2 + (swapY2 * windowSize)

        blankSquare(win, swapX1 * 100, swapY1 * 100, swapX2 * 100, swapY2 * 100)

        layout1 = gridLayout[swapIndex1]
        layout2 = gridLayout[swapIndex2]
        colour1 = colours[swapIndex1]
        colour2 = colours[swapIndex2]
        #CHECKING IF CLICKED TWICE IN THE SAME CELL
        if swapX1==swapX2 and swapY1==swapY2:
            if gridLayout[swapIndex1] == "f":
                penultimate(win, swapX1 * 100, swapY1 * 100, colours[swapIndex1])
                gridLayout[swapIndex1] = "p"
            else:
                finalDigit(win, swapX1 * 100, swapY1 * 100, colours[swapIndex1])
                gridLayout[swapIndex1] = "f"
        #CLICKED IN DIFFERENT CELLS
        else:
            if gridLayout[swapIndex2] == "f":
                finalDigit(win, swapX1 * 100, swapY1 * 100, colours[swapIndex2])
                gridLayout[swapIndex2] = layout1
                colours[swapIndex2] = colour1
            else:
                penultimate(win, swapX1 * 100, swapY1 * 100, colours[swapIndex2])
                gridLayout[swapIndex2] = layout1
                colours[swapIndex2] = colour1

            if gridLayout[swapIndex1] == "f":
                finalDigit(win, swapX2 * 100, swapY2 * 100, colours[swapIndex1])
                gridLayout[swapIndex1] = layout2
                colours[swapIndex1] = colour2
            else:
                penultimate(win, swapX2 * 100, swapY2 * 100, colours[swapIndex1])
                gridLayout[swapIndex1] = layout2
                colours[swapIndex1] = colour2


main()


