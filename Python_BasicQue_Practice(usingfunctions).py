a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))
num = int(input("Enter number"))
km = int(input("Enter value of km"))
celsius = int(input("Enter temperature in celsius"))

#1Arithmetic Programming for addition
def add():
    print("Addition of a and b is",a+b)
add()

#2Arithmetic Programming for Multiplication
def mul():
    print("Multiplication of a and b is",a*b)
mul()

#3Arithmetic Programming for division
def div():
    print("Division of a and b is", a/b)
div()

#4Arithmetic Programming for Subtraction
def sub():
    print("Subtracton of a and b is",a-b)
sub()

#5Program to calculate Area of Triangle
def triangleArea():
    print("Area of Triangle is",0.5*a*b)
triangleArea()

#6Program to calculate Area of Rectangle
def RectArea():
    print("Area of Rectangle is",a*b)
RectArea()

#7Program to calculate Area of Square
def SqArea():
    print("Area of Square is",a*a)
SqArea()

#8Program to calculate Area of Circle
def CircleArea():
    print("Area of Circle is",3.14*a*a)
CircleArea()

#9Program to calculate Volume of Cuboid
def VolCuboid():
    print("Volume of Cuboid is",a*b*c)                #lenghth = a    width = b      height = c
VolCuboid()

#10Program to calculate Volume of Cube
def VolCube():
    print("Volume of Cube is",a*a*a)
VolCube()

#11Program to calculate Volume of Cone
def VolCone():
    print("Volume of Cone is",(1/3)*3.14*a*a*c)         #radius = a         height = c
VolCone()

#12Program to calculate Volume of Cylinder
def VolCylinder():
    print("Volume of Cylinder",3.14*a*a*c)
VolCylinder()

#13Program to Swap two variables
def SwapVariables(a,b):
    z = a
    a = b
    b = z
    print("Swapped Numbers",a,b)
SwapVariables(a,b)

#14Program to Reverse a three digit number
def Reverse(num):
    rem1=num%10
    num=num//10
    rem2=num%10
    num=num//10
    rem3=num
    reverse=rem1*100+rem2*10+rem3*1
    print("Reversed number is",reverse)
Reverse(num)

#15Program to convert kilometer to meter
def meter():
    meter = km*1000
    print("Meter = ",meter)
meter()

#16Program to convert Celsius to Fahrenheit
def Temperature():
    fahrenheit = (celsius * 1.8) + 32
    print("Temperature in fahrenheit is",fahrenheit)
Temperature()

#17Program to calculate (a+b)^2 and (a-b)^2
def Formula():
    formula1 = (a*a +2*(a*b)+b*b)
    formula2 = (a*a +2*(a*b)-b*b)

    print("(a+b)^2 is",formula1)
    print("(a-b)^2 is",formula2)
Formula()
