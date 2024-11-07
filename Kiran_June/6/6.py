
#Rivision
# When there is true or false mean s it "bool"
# the value of true you can say is 1
# and the value of false is 0

#Frozenset
s={1,2,3,4,5,6,7,8,9,10,11}
print(type(s))#<class 'set'>
s=set([1,2,3,4,5])
print(s)#{1, 2, 3, 4, 5}
print(type(s))#<class 'set'>
#Frozen set
#unordered,mutable,heterogenous collection Immutable elements duplicate are not allowed
s=frozenset([1,2,3,4,5])
print(type(s))#<class 'frozenset'>
print(s)

#************Operator***************

l1=[1,2,3,4,5]
l2=[6,7,8,9]
print(l1+l2)#[1, 2, 3, 4, 5, 6, 7, 8, 9]

s1={1,2,3,4,5,6,7,8,9}
s2={12,23,45,56,78,89}
#print(s1+s2)#typeError: unsupported operand type(s) for +: 'set' and 'set'

t1=(1,2,3,4,5,6,7,8,9,10)
t2=(11,22,33,44,55,66,77,88,99,100,101)
print(t1+t2)#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 101)


d1={"a": 1, "b": 2, "c":3}
d2={"a":1,"e":10,"f":44}
#print(d1+d2)#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

n="Sanket"
n1="Kolhe"
print(n1+n)#KolheSanket

c1=3+10j
c2=3+5j
print(c1+c2)#(6+15j)

n1 = 10
n2 = 2
print(n2*n1)#20

n="Sanket"
n1="Kolhe"
#print(n1*n)#TypeError: can't multiply sequence by non-int of type 'str'

n1 = 10
n2 = 2
print(n1/n2)#5.0

#floor division
n1 = 10
n2 = 3
print(n1//n2)#3

print(-10/3)#-3.3333333333333335
print(-10//3)#-4

print(10/3)#3.3333333333333335
print(10//3)#3

#% gives remainder
#Relational Operator
# >
# <
# >=
# <=
# ==
# !=
print(10>5) #true
print(5>=5) #Treu

print(5==5)
print(5!=5)#False

#Logical Operators
# AND 
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

#OR
print(True or True)#True
print(True or False)#True
print(False or True)#True
print(False or False)#False

#3: NOT 
print(not True)#False
print(not False)#True

#  AND and OR 
print((True and False) or (False and True))  # False
print((True and False) or (True and True))  # True
print((False and False) or (False and True))  # False
print((False and False) or (True and True))  # True

# AND, OR, and NOT
print(not (True and False) or (False and True))  # True
print(not (True and False) or (True and True))  # True
print(not (False and False) or (False and True))  # True
print(not (False and False) or (True and True))  # True

a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# Using logical operators with complex expressions
print((a and b) or (not a and b))  # False
print((a and b) or (a and not b))  # True
print((not a and not b) or (not a and b))  # False
print((not a and not b) or (a and b))  # True

#  Using logical operators with nested expressions
print((a and (b or not a)) or (not (a and b)))  # True
print((a or (b and not a)) and (not (a and b)))  # False

#*************in operator************
l=[11,22,33,44,55]
print(33 in l) 

s="rahul"
print("h" in l)#True

l=[11,22,[1,2],33]
print(1 in l)#False

# Is operator examples

# Example 1: Checking if two variables refer to the same object
a = [1, 2, 3]
b = a
print(a is b)  # True, since a and b refer to the same list object

c = [1, 2, 3]
print(a is c)  # False, since a and c refer to different list objects

# Example 2: Checking if a variable is None
x = None
print(x is None)  # True, since x is None

y = 10
print(y is None)  # False, since y is not None

# Example 3: Checking if a variable is an instance of a specific class
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, MyClass))  # True, since obj is an instance of MyClass

print(isinstance(obj, int))  # False, since obj is not an instance of int

# Example 4: Checking if a variable is an instance of a subclass
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

parent_obj = ParentClass()
child_obj = ChildClass()

print(isinstance(child_obj, ParentClass))  # True, since ChildClass is a subclass of ParentClass

print(isinstance(parent_obj, ChildClass))  # False, since ParentClass is not a subclass of ChildClass

#is operator
# Example 1: Checking if two variables refer to the same object
a = [1, 2, 3]
b = a
print(a is b)  # True, since a and b refer to the same list object

c = [1, 2, 3]
print(a is c)  # False, since a and c refer to different list objects

# Example 2: Checking if a variable is None
x = None
print(x is None)  # True, since x is None

y = 10
print(y is None)  # False, since y is not None

# Example 3: Checking if a variable is an instance of a specific class
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, MyClass))  # True, since obj is an instance of MyClass

print(isinstance(obj, int))  # False, since obj is not an instance of int

# Example 4: Checking if a variable is an instance of a subclass
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

parent_obj = ParentClass()
child_obj = ChildClass()

print(isinstance(child_obj, ParentClass))  # True, since ChildClass is a subclass of ParentClass

print(isinstance(parent_obj, ChildClass))  # False, since ParentClass is not a subclass of ChildClass

d={}
#var[key]=value#to add any variable
d["name"]="Sanket"#{'name': 'Sanket'}
print(d)

d={}
name=input("name: ")
roll=int(input("roll: "))
d["name"]=name#{'name': 'sham'}
d["roll"]=roll
print(d)#{'name': 'Sanket', 'roll': 5256}

s1=[11,22,33]
s2=[11,22,33]
print(s1==s2)#true

s1=[11,22,33]
s2=[11,22,33]
print(s1 is s2)#false

# Roll 1,Roll 2
# name
# city,
# percntae
# marks=2 subject

d = {}#---------->lecture number 6-june 1:30 minute important
for i in range(2):
    details={}
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    city = input("Enter City: ")
    details["name"]=name
    details["city"]=city
    d[roll] = details
print(d)#{'5252': {'name': 'Sanket', 'city': 'pune'}, '5698': {'name': 'sham', 'city': 'nagar'}}

d = {}
for i in range(2):
    details={}
    name = input("Enter Name: ")
    roll = eval(input("Enter Roll: "))
    percent=eval(input("Enter Percent: "))
    marks =eval(input("Enter marks: "))
    details["name"]=name
    details["percent"]=percent
    details["marks"]=marks
    d[roll] = details
print(d)#{'2': {'name': 'sham', 'city': 'pune'}, '3': {'name': 'rahul', 'city': 'nagar'}}

#details={1:{"name":"madhav","percent":91,"marks":{"maths":56}}}
details={}
nu=int(input("number of time: "))
for i in range(nu):
    d={}
    r=input("Enter roll: ")
    name=input("name: ")
    city=input("city: ")
    per=input("percentage: ")
    m=eval(input("math: "))
    s=eval(input("science: "))
    marks["math"]=m
    marks["science"]=s
    print(marks)
    d["name"]=name
    d["city"]=city
    d["percentage"]=per
    d["marks"]=marks
    print(d)