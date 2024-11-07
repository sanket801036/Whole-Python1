#Abstration:-Showing neccesary data and hiding implemention
#The process by which function are defined in such a way that only essential details can be seen unnecessary implemention are hidden is called data abstraction

#abstraction in python 
# ---abc module--ABC class,abstractmethod
"""
from abc import ABC,abstractmethod
from abc import*#also u can use

class Test(ABC):
    abstract method
    concrete method
"""

# abstract method:
# --abstract method has only declaration but not implemention
## declaration:
# @abstractmethod
# def m1(self):
#     pass

# --if diff implemention in each sub class then create abstract method
# from abc import *
# class tata(ABC):
#     @abstractmethoddef 
#     def mileage(self):
#         pass
# class nexon(tata):
#     def milage(self):
#         print("milage is 60")
# class safari(tata):
#     def mileage(self):
#         print("mileage is 40")

# abstract class:#abstrsct ka ham log object nhi bana skte
# some time implemention of a class is not com[lete ,such type of partially implemention classes are called abstract class

# --every abstract class in python should be derived from ABC class which is present in abc module

#case1:
from abc import *
class test:
    pass

t=test()#nothing output is giving so it is not abstrac t class
#In above code we can create object for test class bz it it concrete class and if does not contain ANY method

# case2
from abc import *
class Test(ABC):
    pass
t=test()

# -In the above code we can create object, even it is derived from abc class, bz it does not contain any abstract method

#case3:-
from abc import * 
class test(ABC):
    @abstractmethod
    def m1(self):
        pass
#t=test()#--we can't create object of abstract clas

from abc import *
class Test:
    @abstractmethod
    def m1(self):
        print('hello')
t=Test()#hello
t.m1()

from abc import *
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def colour(self):
        print("colour is white")
class Tata(Car):
    def mileage(self):
        print("Tata mileage is 60")
class Suzuki(Car):
    def mileage(self):
        print("Suzuki mileage is 50")
class Honda(Car):
    def mileage(self):
        print("Honda mileage is 30")
#c=Car()# Can't instantiate abstract class Car without an implementation for abstract method 'mileage'#iske andar abstract method hai isliye object nhi bana pa rahe hai kyuki abstract method ke andr partial implementation hota hai
c1=Tata()
c1.mileage()#mileage is 60
c1.colour()#colour is white
c2=Suzuki()
c2.mileage()#Suzuki mileage is 50
c2.colour()#colour is white



#if a class contain atleast one abstract mrethod and if we are extending ABC class then implementation is no possible

#parent class abstract methods should be implementation in the child classes other     we can't initiate child class, if we are not creating child class object then we don't  any error

#Interview Question:
# what is abstraction
# what 
# is abstract class 
# what is abstract method
# how we can achieve abstraction in python