#Revision

# 1. `filter()`
#The filter() function takes two arguments: a function and an iterable. It constructs an iterator from those elements of the iterable for which the function returns true.

#### Example:
# A simple function that checks if a number is even
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

### 2. `map()`
#The `map()` function applies a given function to all the items in an iterable (like a list) and returns a map object (an iterator).
# A simple function that squares a number
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]


### 3. `reduce()`
#The `reduce()` function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in the `functools` module.

#### Example:

from functools import reduce#when we using re function we need to import it from functional tool ootherwise it will show error

l = [1, 2, 3]
sum_val = reduce(lambda x, y: x + y, l)
print(sum_val)
print()

print("*********OOP***********")
### Sequential Programming
#Sequential programming involves writing code in a linear, step-by-step manner

n = [1, 2, 3, 4, 5]
s = 0
for num in numbers:
    s += num * num
print()  # Output: 55

### Functional Programming
#Functional programming involves using pure functions and avoiding shared state or mutable data.
numbers = [1, 2, 3, 4, 5]
def square(num):
    return num * num
# Using map() and sum() to calculate sum of squares
sum_of_squares = sum(map(square, numbers))
print(sum_of_squares)  # Output: 55

### Object-Oriented Programming
#Object-oriented programming involves encapsulating data and behavior into objects.
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def square(self, num):
        return num * num

    def sum_of_squares(self):
        sum = 0
        for num in self.numbers:
            sum += self.square(num)
        return sum

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Create an instance of Calculator
calc = Calculator(numbers)

# Calculate sum of squares
print(calc.sum_of_squares())  # Output: 55

### Summary
# 1. **Sequential Programming**: Straightforward, linear approach with loops and basic control structures.
# 2. **Functional Programming**: Emphasizes pure functions, higher-order functions, and immutability.
# 3. **Object-Oriented Programming**: Encapsulates data and behavior within classes and objects.

#Each paradigm has its strengths and use cases, and choosing the right one depends on the problem at hand and the desired code organization.

# Q1)What is oop in python? =>Object-Oriented Programming (OOP) in Python is a programming paradigm(way of programming) that uses objects, which are instances of classes, to organize code. In Python, everything is an object, and OOP allows you to structure your code in a way that models real-world entities and their interactions.

#class
# object
# reference variable
#20:06



# Object method
class student:
    def init(self):
        print("welcome to constructor")
    def details(self):
        print("welcome to details method")

s1=student()
s1.details()
s1.details()
s1.details()

# constructor is special method.
# there is no need to call constructor.
# It is use to initilization.
# init method.



class student:
    def init(self):
        print(f"id of self is{id(self)}")

s1=student()
print(f"id of self is{id(s1)}")

s2=student()
print(f"id of self is{id(s2)}")

