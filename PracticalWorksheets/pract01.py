# Practical Worksheet 1: Getting started with Python
# angus, 855751

def sayHello():
    print("Hello world")

def count():
    for i in range(10):
        print(i)

def kilos2pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)

def sayName():
    print("angus")
    
def sayHello2():
    print("Hello")
    print("World")

def euros2pounds():
    eurosInput = int(input("Enter the amount in euros > > "))
    poundsOutput = eurosInput / 1.09
    print(eurosInput, "Euros is equal to " + str(poundsOutput) + " Pounds")
    
def addUp():
    x=int(input("Enter the first number > > "))
    y=int(input("Enter the second number > > "))
    print(x+y)
    
def changeCounter():
    onePence = int(input("How many 1p coins? > > "))
    twoPence = int(input("How many 2p coins? > > "))
    fivePence = int(input("How many 5p coins? > > "))
    totalPence = onePence + (twoPence * 2) + (fivePence * 5)
    print("You have " + str(totalPence) + " pence")

def tenHellos():
    for i in range(10):
        print("Hello")

def count2():
    for i in range(10):
        print(i+1)

def weightsTable():
    for i in range(11):
        kgs = i*10
        lbs = kgs*2.2
        print(kgs,"kgs <->",round(lbs,1),"lbs")
    
def futureValue():
    money = int(input("amount of investments? (£) >> "))
    years = int(input("length of investment? (years) > > "))
    for i in range(years):
        money = money * 1.055
        
    print("£" + str(round(money, 2)))

    
weightsTable()
    
    
    
    
    
    
    
    
    
    
    
    
    
    