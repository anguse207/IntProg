from graphics import *

def stop(win):
    win.getMouse()
    win.close()

def circles():
    win = GraphWin("Circles",400,100)
    for i in range(24):
        p = win.getMouse()
        circle = Circle(Point(p.getX(),p.getY()),10)
        if p.getX() >= 300:
            circle.setFill("Blue")
            circle.draw(win)
            
        elif p.getX() >= 200:
            circle.setFill("Green")
            circle.draw(win)
        
        else:
            circle.draw(win)
    
    stop(win)

def circles2():
    win = GraphWin("Circles",400,100)
    for y in range(5):
        for i in range(5):
            p = win.getMouse()
            circle = Circle(Point(90-i*20,10+y*20),10)
            if p.getX() >= 300:
                circle.setFill("Blue")
                circle.draw(win)
                
            elif p.getX() >= 200:
                circle.setFill("Green")
                circle.draw(win)
            
            else:
                circle.draw(win)                
    
    stop(win)


circles2()
