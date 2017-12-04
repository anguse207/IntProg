import math

def types():
    print(type(3))
    print(type(-64))
    print(type(53.2173))
    print(type(3.0))
    print(type(123456789123456789))
    print(type("hello"))
    print(type("123"))
    print(type('123'))
    print(type(True))
    print(type("False"))
    
def circumferenceOfCircle():
    radius = int(input("Enter the radius of the circle > > "))
    circumference = ((2*math.pi)*radius)
    circumference = round(circumference,2)
    print("The circumference of the circle is", circumference)
    
def areaOfCircle():
    radius = int(input("Enter the radius of the circle > > "))
    area = (math.pi*(radius**2))
    area = round(area,2)
    print("The area of the circle is", area)

def costOfPizza():
    pizDia = int(input("Enter the diameter of a pizza (in centimeters) > > "))
    pizRad = pizDia / 2
    pizArea = (math.pi*(pizRad**2))
    ingredientCost = round(pizArea*1.5)
    print("The cost of the pizza is £" + str(ingredientCost/100))

def slopeOfLine():
    x1 = int(input("Please input the first value of x > > "))
    x2 = int(input("Please input the second value of x > > "))
    y1 = int(input("Please input the first value of y > > "))
    y2 = int(input("Please input the second value of y > > "))
    gradient = round((y2-y1)/(x2-x1),2)
    print("The gradient of the line is",gradient)

def distanceBetweenPoints():
    x1 = int(input("Please input the first value of x > > "))
    x2 = int(input("Please input the second value of x > > "))
    y1 = int(input("Please input the first value of y > > "))
    y2 = int(input("Please input the second value of y > > "))
    distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
    print("The distance between the points is", distance)
    
def travelStatistics():
    avgSpeed = int(input("Enter the average speed (km/hour) > > "))
    duration = int(input("Enter the duration (hours) > > "))
    distance = round((avgSpeed*duration),2)
    print("The distance travelled is",str(distance) + " Km")
    fuelUsed = distance // 5
    print("The amount of fuel used is",str(fuelUsed) + " Litres")
    
def sumOfNumbers():
    total = 0
    n = int(input("n = "))
    for i in range(n):
        total = total+(i+1)
        
    print(total)
    
def averageOfNumbers():
    amountValues = int(input("how many numbers to average > > "))
    print("Enter the",amountValues,"values 1 after each other")
    total = 0
    for i in range(amountValues):
        averageInput = int(input("> > "))
        total += averageInput
        
    average = total/amountValues
    print("The average of the values is",average) 

def selectCoins():
    totalAmount = int(input("Enter an amount in pence > > "))
    
    amountLeft = totalAmount % 200
    twoPounds = totalAmount // 200
    
    onePounds = amountLeft // 100
    amountLeft = totalAmount % 100
    
    fiftyPence = amountLeft // 50
    amountLeft = totalAmount % 50
    
    twentyPence = amountLeft // 20
    amountLeft = totalAmount % 20
    
    tenPence = amountLeft // 10
    amountLeft = totalAmount % 10
    
    fivePence = amountLeft // 5
    amountLeft = totalAmount % 5
    
    twoPence = amountLeft // 2
    amountLeft = totalAmount % 2
    
    onePence = amountLeft // 1
    amountLeft = totalAmount % 1
    
    
    print(twoPounds , " x £2 , " , onePounds , " x £1 , " , fiftyPence , " x 50p , " , twentyPence , " x 20p , " , tenPence , " x 10p , " , fivePence , " x £5 , " , twoPence , " x 2p , " , onePence , " x 1p")

        
    
selectCoins()
        
    



    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    