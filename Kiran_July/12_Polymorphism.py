# PolyMorphism
n1=10
n2=20
print(n1+n2)#30
print(n1.__add__(n2))#30
print(dir(n1))#show attributes of an abject

s1="raj"
s2="patil"
print(s1+s2)#rajpatil
print(dir(s1))#show attributes of an abject

# OverLoading
# 1)Method overloading
# 2)Operator overloading
class Book:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages
    
b1=Book('xyz',100)
b2=Book("abc",200)
print(b1.pages)#100
print(b2.pages)#200
print(b2.pages+b2.pages)#300
print()

class Book:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return total
    
b1=Book('xyz',100)
b2=Book("abc",200)
print(b1+b2)#300
print(b1.__add__(b2))
print()

class Book:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return Book("mix",total)
    def __str__(self):
        return f"{self.pages}"
    
b1=Book('xyz',100)
b2=Book("abc",200)
b3=Book("pqr",500)
print(b1+b2+b3)#800

print("*****Method overloading*****")#usi class ko usike andar redefined krna
# class Calci:
#     def add(n1,n2):
#         return n1+n2

# c=Calci()
# c.add(10,20)#30
# c.add("vaibhav","patil")#erroe in it

print("*****Method over-riding*****")#redefind parent class into child class
class Parent:
    def property(self):
        print("Gold,Home,Farm")
    def marry(self):
        print("mamachi mulgi")

class Child(Parent):
    def my_property(self):
        print("Bike,flat")
    def marry(self):
        print("xyz")
c=Child()
c.property()#Gold,Home,Farm
c.my_property()#Bike,flat
c.marry()#xyz

#***variable overriding********
class Parent:
    course="java"

class Child:
    pass
c=Child()
print(c.course)

#Symmary
# PolyMorphism
# Overloading
#     >Operator
#     >method
# overriding
#     >method
#     >variable
