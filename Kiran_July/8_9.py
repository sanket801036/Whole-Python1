#Pillars of objects oriented programming
# Inheritance
# PolyMorphism
# abstraction
# encapsulation

# *******************Inheritance*************************
#Q6)what is an Inheritance in oop?

# =>The ability of a class to inherit properties and methods from another class.It promotes code reuse and allows you to create a hierarchy of classes.
# OR we can say
# =>Inheritance is a fundamental concept in object-oriented programming Ex (OOP) that allows a new class (subclass or derived class) to inherit attributes Encaps and methods from an existing class (superclass or base class).

### 1. Single/simple Inheritance
#A class inherits from a single parent class.
#single Inheritance:
#=>In single inheritance, a subclass inherits from only one superclass. This is the simplest form of inheritance. A class can have only one immediate parent class.

class Parent:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Parent name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Child name: {self.name}, Age: {self.age}")

# Example usage
c = Child("Alice", 10)
c.display()  # Output: Parent name: Alice
c.show()     # Output: Child name: Alice, Age: 10
print()

#Example 2
class Parent:
    def m1(self):
        print("welcome to m1 method of Parent class")
class Child(Parent):
    def m2(self):
        print("welcome to m2 method of child class")
c=Child()
c.m2()#welcome to m2 method of child class
c.m1() #welcome to m1 method of Parent class


### 2. Multiple Inheritance
#A class inherits from multiple parent classes.
#Multiple Inheritance: =>In multiple inheritance, a subclass can inherit from more than one superclass. =>This allows the subclass to inherit attributes and methods from multiple classes.

class Parent1:
    def function1(self):
        print("This is Parent1")

class Parent2:
    def function2(self):
        print("This is Parent2")

class Child(Parent1, Parent2):
    def function3(self):
        print("This is Child")

# Example usage
c = Child()
c.function1()  # Output: This is Parent1
c.function2()  # Output: This is Parent2
c.function3()  # Output: This is Child


### 3. Multilevel Inheritance
#A class is derived from a class that is also derived from another class.
##=>In multilevel inheritance, a subclass inherits from another subclass, creating a chain or hierarchy of classes. =>Each subclass extends the one above it.

class Grandparent:
    def function1(self):
        print("This is Grandparent")

class Parent(Grandparent):
    def function2(self):
        print("This is Parent")

class Child(Parent):
    def function3(self):
        print("This is Child")

# Example usage
c = Child()
c.function1()  # Output: This is Grandparent
c.function2()  # Output: This is Parent
c.function3()  # Output: This is Child

print("#Example 2:")
class GP:
    def m1(self):
        print("I am m1 method of GP class")
class parent(GP):
    def m2(self):
        print("I am m2 method in parent class")
class child(parent):
    def m3(self):
        print("I am m³ method of child class")
c = child()
c.m1()#I am m1 method of GP class
c.m2()#I am m2 method in parent class
c.m3()#I am m³ method of child class

### 4. Hierarchical Inheritance
#Multiple classes inherit from the same parent class.

class Parent:
    def function(self):
        print("This is Parent")

class Child1(Parent):
    def function1(self):
        print("This is Child1")

class Child2(Parent):
    def function2(self):
        print("This is Child2")

# Example usage
c1 = Child1()
c2 = Child2()

c1.function()   # Output: This is Parent
c1.function1()  # Output: This is Child1

c2.function()   # Output: This is Parent
c2.function2()  # Output: This is Child2



### 5. Hybrid Inheritance
#A combination of two or more types of inheritance.
class Grandparent:
    def function1(self):
        print("This is Grandparent")

class Parent1(Grandparent):
    def function2(self):
        print("This is Parent1")

class Parent2:
    def function3(self):
        print("This is Parent2")

class Child(Parent1, Parent2):
    def function4(self):
        print("This is Child")

# Example usage
c = Child()
c.function1()  # Output: This is Grandparent
c.function2()  # Output: This is Parent1
c.function3()  # Output: This is Parent2
c.function4()  # Output: This is Child
print("------------------------")
"""
class Polygon:
    def __init__(self,no_side):
        self.no_side=no_side
        self.lengthofsides=[]
    def input_side(self):
        for i in range(1,self.no_side+1):
            s=eval(input(f"enter side {i}="))
            self.lengthofsides.append(s)
        print(self.lengthofsides)
    def display(self):
        for i in range(len(self.lengthofsides)):
            print(f"length of s{i+1}: {self.lengthofsides[i]}")

class perimeter(Polygon):
    def __init__(self,no_sides):
        Polygon.__init__(self,no_sides)
    def peri_triangle(self):
        s1,s2,s3=self.lengthofsides
        perimeter=s1+s2+53
        print('Perimeter of triangle', perimeter)
    def peri_rectangle(self):
        perimeter=0
        for i in self.lengthofsides:
            perimeter+=i
            print("perimeter of rectangle", perimeter)

triangle=perimeter(3)
triangle.input_side()
triangle.peri_triangle()
"""

#Problem 1:
#Create a class called "Book" that has attributes for title,author and description for title,author, and publication year. The class should have a method to display the book's information

class Book(self,tile,author,year):
    self.title =title
    self.author = author
    self.year = year
print(Book)

#Problem 2:
# Create a class called "Student" that has attributes for name,roll number,and grades.The class should have a method to calculate the average grade.
