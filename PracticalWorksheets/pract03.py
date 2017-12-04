# Practical Worksheet 3: Graphical Programming
# your name, your number

from graphics import *

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    lleg = Line(Point(100, 120), Point(110, 160))
    lleg.draw(win)
    rleg = Line(Point(100, 120), Point(90, 160))
    rleg.draw(win)
    arms = Line(Point(80, 90), Point(120, 90))
    arms.draw(win)
    
    win.getMouse()
    win.close()

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
    
    win.getMouse()
    win.close()
    
def drawCircle():
    radiusInput = eval(input("Radius of circle? > > "))
    win = GraphWin("Draw Circle")
    c = Circle(Point(100,100),radiusInput)
    c.draw(win)

    win.getMouse()
    win.close()
    
def drawArcheryTarget():
    win = GraphWin("Draw Archery Target")
    
    yellowCircle = Circle(Point(100,100),30)
    redCircle = Circle(Point(100,100),60)
    blueCircle = Circle(Point(100,100),90)
    
    yellowCircle.setFill("yellow")
    redCircle.setFill("red")
    blueCircle.setFill("blue")
    
    blueCircle.draw(win)
    redCircle.draw(win)
    yellowCircle.draw(win)
    
    win.getMouse()
    win.close()
    
def drawRectangle():
    win = GraphWin("Draw Rectangle")
    
    xInput = eval(input("x = "))
    yInput = eval(input("y = "))
    
    x1 = (200-xInput)/2
    x2 = x1 + xInput
    
    y1 = (200-yInput)/2
    y2 = y1 + yInput
    
    rectangle = Rectangle(Point(x1,y1), Point(x2,y2))
    rectangle.draw(win)
    
    win.getMouse()
    win.close()
    
def blueCircle():
    win = GraphWin("Blue Circle")
    p = win.getMouse()
    blueCircle = Circle(Point(p.getX(),p.getY()),50)
    blueCircle.setFill("Blue")
    blueCircle.draw(win)
    
    win.getMouse()
    win.close()
    
def tenLines():
    win = GraphWin("Ten Lines")
    for i in range(10):
        message = Text(Point(100,100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")
    
    win.getMouse()
    win.close()
    
def tenStrings():
    win = GraphWin("Ten Strings",300,300)
    for i in range(10):
        hint = Text(Point(20,20), "Click where you want your message")
        hint.draw(win)
        message = input("Enter a message to plot > > ")
        
        
    win.getMouse()
    win.close()
    
def tenColouredRectangles():
    win = GraphWin("Ten Coloured Rectangles",300,300)
    for i in range(10):
        #hint = Text(Point(4,4), "Click the top left point")
        #hint.draw(win)
        p1 = win.getMouse()
        print(p1)
        p2 = win.getMouse()
        rectangle = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
        
        rectangle.draw(win)
        
    win.getMouse()
    win.close()
        

tenLines()



























































































































