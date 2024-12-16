"""print()
#int()
#len()
"""
#custom function

def sayHello():
    print('hello')

sayHello()

#function parameter

def sayHelloTo(name):
    print(f"hello {name}")

sayHelloTo("eric")

def getRectangleArea(width, height):
    area = width*height
    print(f"The area is {area}")

getRectangleArea(2,4)

#default parameter
#if need to count many area

def getRectangleArea(width, height = 10): #default
    area = width*height
    return area

r1 = getRectangleArea(2,5)
r2 = getRectangleArea(3,5)
print(f"The total area is {r1+r2}")

#return statement, calculate 2 square area r1 and r2

#vaiable scope
outside = "outside"
def printVar():
    print(f'{outside}')

printVar()

outside = "outside" #global scope
inside = "inside" #global scope
def printVar():
    inside = "inside" #vaiable scope

    print(f'{outside} {inside}')

printVar()
print(inside)