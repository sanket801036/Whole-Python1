Check Your Answers
1) Which of the following is true about inheritance in Python?
Python supports only single inheritance.
Python supports only multiple inheritance.
Python supports both single and multiple inheritance.
Python doesn't support inheritance.
Your Answer: 3
Correct Answer: 3

2) In Python, which method is automatically called when an object is created?
create()
init()
constructor()
details()
Your Answer: 2
Correct Answer: 2

3) What is the correct syntax to create a constructor in Python?
def __init__(self):
def constructor(self):
def init(self):
constructor init(self):
Your Answer: 1
Correct Answer: 1

4) Which of the following is true about method overloading in Python?
Method overloading allows a subclass to provide a specific implementation of a method that is already provided by its superclass.
Method overloading allows a superclass to provide a specific implementation of a method that is already provided by its subclass.
Python does not support method overloading.
Method overloading is the process of providing multiple implementations of a method with the same name but different parameters.
Your Answer: 1
Correct Answer: 3

5) What is the output of the following code?
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 4)
print("Area of rectangle:", rect.area())
 

9
20
18
25
Your Answer: 2
Correct Answer: 2

6) Which of the following statements is true about static variables in Python?
static variables are declared inside a method.
static variables are declared inside a class but outside any method.
static variables are declared using the static keyword.
static variables are the same for all instances of a class.
Your Answer: 1
Correct Answer: 2

7) Which of the following is true about method overriding in Python?
It is not possible to override a method in Python.
Method overriding allows a subclass to provide a specific implementation of a method that is already provided by its superclass.
Method overriding allows a superclass to provide a specific implementation of a method that is already provided by its subclass.
Method overriding is only possible when the superclass and subclass are in different modules.
Your Answer: 3
Correct Answer: 2

8) Which of the following is true about encapsulation in Python?
Encapsulation is the process of combining data and functions into a single unit.
Encapsulation allows a class to inherit from multiple base classes.
Encapsulation is the process of hiding the implementation details of a class.
Encapsulation is only possible with private methods in Python
Your Answer: 3
Correct Answer: 3

9) What is the output of the following code?
class A:
    def __init__(self):
        self.__x = 10

obj = A()
print(obj.__x)
 

10
Error: 'A' object has no attribute '__x'
Error: '__x' is a private variable
Error: 'A' object has no attribute '_A__x'
Your Answer: 1
Correct Answer: 2

10) What is the output of the following code?
class MyClass:
    x = 5

obj = MyClass()
print(obj.x)
 

0
5
MyClass
None of the above
Your Answer: 2
Correct Answer: 2

11) Which of the following is not a pillar of object-oriented programming?
Inheritance
Encapsulation
Polymorphism
Modularity
Your Answer: 4
Correct Answer: 4

12) What is the output of the following code?
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

obj = B()
print(obj.x, obj.y)
 

1 1
1 2
2 1
2 2
Your Answer: 2
Correct Answer: 2

13) Which of the following is used to call a method of the base class from a derived class in Python?
base.method()
super().method()
this.method()
parent.method()
Your Answer: 2
Correct Answer: 2

14) What is the output of the following code?
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

class C(B):
    def __init__(self):
        super().__init__()
        self.z = 3

obj = C()
print(obj.x, obj.y, obj.z)
 

1 2 3
1 3 2
3 2 1
2 1 3
Your Answer: 1
Correct Answer: 1

15) Which keyword is used to define a class in Python?
class
Class
define
def
Your Answer: 2
Correct Answer: 1

16) In Python, how can we create private variables?
By using the private keyword
By using the protected keyword
By prefixing the variable name with two underscores (__)
By prefixing the variable name with one underscore (_)
Your Answer: 4
Correct Answer: 3

17) What is the output of the following code?
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

def polymorphism(obj):
    obj.method()

obj1 = A()
obj2 = B()

polymorphism(obj1)
polymorphism(obj2)
 

A method B method
B method A method
A method A method
B method B method
Your Answer: 1
Correct Answer: 1

18) what is the purpose of self?
it refers to the current instance of the class.
It refers to the current method being executed.
It is used to call another method in the class.
It is a keyword used to define a class.
Your Answer: 1
Correct Answer: 1

19) What is the output of the following code?
class A:
    def method(self, x):
        print("A method with one parameter")

    def method(self, x, y):
        print("A method with two parameters")

obj = A()
obj.method(1, 2)
 

A method with one parameter
A method with two parameters
Error: method() takes 2 positional arguments but 3 were given
Error: method() missing 1 required positional argument: 'y'
Your Answer: 2
Correct Answer: 2

20) Which of the following statements is true about polymorphism in Python?
 

Polymorphism allows a subclass to provide a specific implementation of a method that is already provided by its superclass.
Polymorphism allows a superclass to provide a specific implementation of a method that is already provided by its subclass.
Polymorphism allows a function to have different forms based on the number or type of parameters.
Polymorphism is the process of hiding the implementation details of a class.A
Your Answer: 3
Correct Answer: 3

21) What is the output of the following code?
class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(obj.x)
 

0
10
MyClass
None of the above
Your Answer: 2
Correct Answer: 2

22) Which of the following is true about class variables in Python?
Class variables are the same for all instances of a class.
Class variables are declared inside a method.
Class variables are declared using the self keyword.
Class variables are declared using the instance keyword
Your Answer: 3
Correct Answer: 1

23) What is the output of the following code?
class Dog:
    species = 'mammal'

    def __init__(self, name):
        self.name = name

pet1 = Dog("Buddy")
pet2 = Dog("Max")

print(pet1.name + " is a " + pet1.species)
print(pet2.name + " is a " + pet2.species)
 

Buddy is a mammal Max is a mammal
Buddy is a mammal Buddy is a mammal
Max is a mammal Max is a mammal
Buddy is a mammal Max is a mammal
Your Answer: 4
Correct Answer: 1

24) What is the output of the following code?
class A:
    def __init__(self, x=5):
        self.x = x

obj1 = A()
obj2 = A(10)

print(obj1.x, obj2.x)
 

5 10
10 10
0 0
10 5
Your Answer: 1
Correct Answer: 1

25) What is the correct syntax to create an object of a class in Python?
object = Class()
object = new Class()
object = create Class()
object = Object(Class)
Your Answer: 4
Correct Answer: 1

