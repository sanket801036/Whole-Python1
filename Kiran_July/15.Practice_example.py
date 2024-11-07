#Practice Example
class Product:
    def __init__(self,product_id,name,quantity,price_per_unit):#cunsturctor kr andar jo likha hai usko parameter kte hai
        self.product_id = product_id            #initialize krna(instance variable)
        self.name=name                          #initialize krna(instance variable)
        self.quantity=quantity                  #initialize krna(instance variable)
        self.price_per_unit=price_per_unit      #initialize krna(instance variable) 
    
    def update_quantity(self,new_quantity):
        self.quantity = new_quantity

    def calculate_value(self):
        return self.quantity*self.price_per_unit

product1=Product("Poor","Laptop",100,800)
print("Current value.",product1.calculate_value())#Current value. 80000
product1.update_quantity(120)
print("Update value:",product1.calculate_value())#Update value: 96000

class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1 * num2
    def divide(self,num1,num2):
        if num2==0:
            return "Cannot divide by zero"
        return num1 / num2
calculator=Calculator()
print("Addition:",calculator.add(5,3))#Addition: 8
print("Subtraction:",calculator.subtract(5,3))#Subtraction: 2
print("Multiplication:",calculator.multiply(5,3))#Multiplication: 15
print("Division:",calculator.divide(5,3))#Division: 1.6666666666666667

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def is_square(self):
        return self.length==self.width

rectangle1=Rectangle(5,3)
print("Area: ",rectangle1.area())#Area:  15
print("Perimeter: ",rectangle1.perimeter())#Area:  15
print("is_square? ",rectangle1.is_square())#is_square?  False
print()

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def circumference(self):
        return 2* math.pi*self.radius

circle1=Circle(5)
print("Area",circle1.area())#Area 78.53981633974483
print("circumference",circle1.circumference())#circumference 31.41592653589793

class Procuct:
    def __init__(self,product_id,name,price,quantity_available):
        self.product_id = product_id
        self.name = name
        self.price=price
        self.quantity_available = quantity_available

    def purchese(self,quantity):
        if quantity <=self.quantity_available:
            self.quantity_available -= quantity
            return f"Purchase syccessful! Total cost:${quantity*self.price}"
        else:
            return "Sorry,product not available in desired quantity"

    def check_availability(self):
        return f"Available quantity:{self.quantity_available}"

product1=Product("Poor","Laptop",800,10)

print(product1.check_availability())
print(product1.purchase(3))
print(product1.check_availability())


