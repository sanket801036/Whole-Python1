 #Rivision
#  class:-blueprint to construct object
#     class Class_name:
#         pass

#  object:-instance of class
#     Class_name()
    
#  ref veriable:-used to access function of an object
#     r_var=class_name,

# Q)What is constructor:- In OOP, a constructor is a special method class tha is automatically called when an object of a class is instantiated.Constructor are used to initialize the attributes or properties of an object.
class Student:
    def __init__(self):#self is an reference variable#self is a reference variable it is used to access the functionality of the of object onside of the class

        print(f"id of self is {id(self)}")#id of self is 1784824660240#id of self is 1316022387296

s1=Student()#iska reference self mein ja raha hai#si is a reference variable it is used to access the functionality of the of object outside of the class
print(f"id of s1 is {id(s1)}")#id of s1 is 1784824660240#as you can see both id's are same
s2=Student()
print(f"id of s2 is {id(s2)}")#id of s2 is 1316022387296 


#**Attributes**(it also a variable)
#Variable that store data within a class.They represent characteristics or properties of an object.
 #   name = "rehul"

# 1. instance variable************************************************************************************
# 1) instance variable
# => Variables that belong to instances (objects) of a class.
# => Specific to each instance of the class.
# => Defined within methods using self.
# => Separate copy is created for all object
# => Object variable is not shared between object
# => A change made to the instance variable by one object will not be reflected
# in other object


# variable that is defined within a class and is unique to each instance (object) of that class. 
# Instance variables are created when an object is instantiated from the class and are accessible through the object's reference variable.

# `name` is an instance variable of the `Student` class. When `s1` and `s2` are instances of `Student`, they each have their own unique `name` attribute.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
s2 = Student("Jane")

print(s1.name)  # Output: John
print(s2.name)  # Output: Jane

class Student:
    def __init__(self, name,age,city):
        self.name = name               #instance variable is name
        self.age = age                 #instance variable is age
        self.city = city               #instance variable is city
s1 = Student("vjay","25",'pune')
print(s1.name)#vjay
s2 = Student("ajay","24","nashik")
print(s2.age)#24
s1.name = "sanket"
print(s1.name)#sanket
print(s2.name)#ajay
print()
# `s1` and `s2` each has its own `name` attribute. The `name` attribute is an instance variable, as it is defined within the `__init__` method and is accessed through the object's reference variable (`s1` and `s2`).

# 2.class/static vairiable*******************************************************************************

#A variable that is shared among all instances of a class. It is defined within the class but outside of any method. Static variables are created when the class is defined and are accessible through the class name, not through an instance of the class.

#Static variables are useful when you want to store data that is common to all instances of a class, such as a counter or a constant value.

class Student:
    count = 0  # Static variable
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("John")
s2 = Student("Jane")

print(Student.count)  # Output: 2
print(s1.count)       # Output: 2
print(s2.count)       # Output: 2

#In this example, `count` is a static variable that keeps track of the number of instances of the `Student` class. It is incremented each time a new instance is created.

# Static variables can also be accessed directly through the class name, as shown in the example above.

# Note: Static variables are not specific to individual instances of a class. They are shared among all instances and can be modified by any instance or the class itself.

#Example from academy
# 2)static/class variable
# => variable which is define inside class and outside of any method
# => Variables that are shared among all instances of a class.
# => Common to all instances of the class.
# => When any value is common for all objects then we create static variable
# to store these value =>we can access by using ref variable ouside of the class

class Employee:
    def __init__(self,name,department,salary,c_name):
        self.name = name
        self.department = department
        self.salary = salary
        self.c_name = c_name

e1=Employee("raj",'HR',"32000","TCS")
e2=Employee("rajesh","Python",'202020',"TCS")#ismein company name(TCS) to  sabke liye same hai fir memory waste na ho isliye usko object level ka nhi banayenge usko banayenge class level ka exaMPLE AS FOLLOWS

class Employee:
    c_name = "TCS"  #therefore it is class variable
    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        

e1=Employee("raj",'HR',"32000")
e2=Employee("rajesh","Python",'202020')
print(e1.salary)#32000#it is instance variable#instance level
print(e2.name)#rajesh#it is instance variable#instance level
print(e1.c_name)#TCS#it is static variable##class level
print(e2.c_name)#TCS#it is static variable#class level
print(Employee.c_name)#TCS#it is static variable#class level
Employee.c_name = "infosys"
print(e1.c_name)#infosys
print(e2.c_name)#infosys

# # 3.local vairiable