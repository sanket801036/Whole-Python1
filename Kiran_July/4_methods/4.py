#Revision:-
# Q1) What is oop in python?
# =>It is a programming paradigm that uses objects, which are instances of classes, to organize code. In Python, everything is an object, and OOP allows you to structure your code in a way that models real-world entities and their interactions.

# # 3.local vairiable****************************************************
# => Variables defined within a method of a class.
# => Limited to the method where it is defined.
class Calci:
    def sum(self,n1,n2):#here n1 and n2 is local varible
        return n1 + n2
c1 = Calci()
c1.sum(10,20)

def greet(name):
    message = "Hello, " + name
    print(message)

greet("John")#Hello, John
print()
# print(message) # name 'message' is not defined  # This will raise a NameError because 'message' is a local variable in the 'greet' functio

# method:
# => Functions defined within a class that operate on the object's data. They represent the behaviors that an object can perform.
# Methods are used to encapsulate and organize code within a class, making it easier to understand and maintain

# 1.Instance method:*******************************************************************************
# 1)Instance :-
# => A method that operates on an instance of the class. 
# => Defined within the class and takes self as the first parameter.
# => we can access instance method by using ref. variable outside of the class_name only.

class Employee:
    company = 'TKA'
    location = 'krve nagar'

    def __init__(self,name,city,dep,sal):
        self.name = name                    #instance variable
        self.city = city                    #instance variable
        self.dep = dep                      #instance variable
        self.sal = sal                      #instance variable
    def details(self):                      #instance method
        print(f"""
                Name:{self.name} 
                City:{self.city}
                Department:{self.dep}
                Salary :{self.sal}
                Company Name: {self.company}
                """)                        #instance method

e1=Employee("raj","pune","HR",23000)
print(e1.name)#raj
e1.details()                                #to call the instance method

# Output:-        Name:raj
#                City:pune
#                Department:HR
#                Salary :23000
#                Company Name: TKA
e2=Employee("vijay","nashik","mr",340000)
e2.details()
# Output:-        Name:vijay
#                City:nashik
#                Department:mr
#                Salary :340000
#                Company Name: TKA

# An instance method in Python is a function defined within a class that operates on the object's data. They represent the behaviors or actions that an object can perform. Instance methods are called on an instance of the class and have access to the `self` parameter, which represents the current instance.

# Instance methods are defined within a class and have the following characteristics:
# 1. They are defined within a class.
# 2. They are associated with an instance of the class.
# 3. They have access to the instance variables and other methods of the class.
# 4. They have access to the `self` parameter, which represents the current instance.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"Starting the {self.make} {self.model}'s engine.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Calling the instance method
my_car.start_engine()
# Output: Starting the Toyota Camry's engine.

# In the example above, the `start_engine` method is an instance method of the `Car` class. It operates on the instance variables `make` and `model` and prints a message indicating that the engine is starting. The method is called on an instance of the `Car` class (`my_car`) using the dot notation (`my_car.start_engine()`).

# 2.Class methods:*************************************************************************
# iska use kro jab class level ke data pe kam krna ho
# => A method that operates on the class itself rather than on instatnces(works on class level data )
# => It is mandatory to use @classmethod decorator
# => we can access class method by using object reference and class_name but recommended to use class_name only
# A class method in Python is a function defined within a class that operates on the class itself, rather than on an instance of the class. Class methods are associated with the class and can be called on the class itself, without creating an instance of the class. They have access to the class variables and other class-level attributes.

# Class methods are defined using the `@classmethod` decorator and have the following characteristics:
# 1. They are defined within a class.
# 2. They are associated with the class itself, not an instance of the class.
# 3. They have access to the class variables and other class-level attributes.
# 4. They have access to the `cls` parameter, which represents the current class.

class Student:
    total_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1
    @classmethod
    def get_total_students(cls):
        return cls.total_students
s1 = Student("John", 18)
s2 = Student("Alice", 17)

total_students = Student.get_total_students()
print(f"Total students: {total_students}")  # Output: Total students: 2
print("---------------")

# In the example above, the `get_total_students` method is a class method that returns the total number of students created. It operates on the class itself and has access to the `total_students` class variable. The method is called on the class itself using the dot notation (`Student.get_total_students()`).

# Class methods are useful when you want to perform operations that are related to the class as a whole, rather than on individual instances of the class. They can be used to access class variables, perform class-level validations, or implement alternative constructors.

#Example academy:
class Employee:
    company = 'TKA'
    location = 'krve nagar'

    def __init__(self,name,city,dep,sal):
        self.name = name
        self.city = city
        self.dep = dep
        self.sal = sal
    def details(self):
        print(f"""
                Name:{self.name} 
                City:{self.city}
                Department:{self.dep}
                Salary :{self.sal}
                Company Name: {self.company}
                """)
    @classmethod#ye only work krta hai class level ke data pe kam krna ho
    def company_details(cls):
        print(cls.company)#TKA
        print(cls.location)#krve nagar
        #print(cls.name)#AttributeError: type object 'Employee' has no attribute 'name'

e1=Employee("raj","pune","HR",23000)
e2=Employee("vijay","nashik","MR",65000)
e2.company_details()



# 3.Static methods: ****************************************************************************************
#jab apako local data pe kam krna ho to
