# 1. What is a function in Python?*
# - A function in Python is a block of reusable code that performs a specific task. It takes inputs (arguments), performs operations, and  returns a result.

# 2. *How do you define a function in Python?*
#  :- In Python, a function is defined using the def keyword followed by the function name and parameters enclosed in parentheses. For example:
def greet(name):
    print(f"Hello, {name}!")
    # Hello, Alice!
     
# 3. *Explain the syntax for calling a function in Python.*
# To call a function in Python, you simply write the function name followed by parentheses and any required arguments inside the parentheses.
greet("Alice")
# Hello, Alice! 

# 4.What is the difference between return and print in Python functions?
#  print is a Python function that outputs a value to the console, 
#  while return is a statement that exits a function and optionally sends a value back to the caller.
#  print is used for displaying information,
#  while return is used to return values from a function for further use in the program.

# 5. *How do you pass arguments to a function in Python?*
#    - *Answer:* Arguments are passed to a function by placing them inside the parentheses when defining or calling the function. Python supports positional arguments (based on their position) and keyword arguments (based on parameter names).

# 6. *Explain the difference between positional arguments and keyword arguments.*
#    - *Answer:* Positional arguments are passed based on their position in the function call and matched to parameters in the function definition in order. 
# Keyword arguments are identified by parameter names, allowing you to pass arguments in any order.
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# # Using positional arguments
greet("Alice", 30)
#Hello, Alice! You are 30 years old.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# # Using keyword arguments
greet(age=30, name="Alice")
#Hello, Alice! You are 30 years old.

# 7. *What are default arguments in Python functions? Give an example.*
#    - *Answer:* Default arguments in Python functions are parameters that assume a default value if no argument is provided during the function call. Example:
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    greet("Bob")  # Output: Hello, Bob!
 
# 8. **Discuss variable-length arguments (*args and **kwargs) in Python functions.**
#    - *Answer:* *args allows a function to accept any number of positional arguments as a tuple, while **kwargs allows any number of keyword arguments as a dictionary. They are useful when the number of arguments is unknown beforehand.
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

# Using variable-length positional arguments
greet("Alice", "Bob", "Charlie")
#Hello, Alice!
#Hello, Bob!
#Hello, Charlie!

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using variable-length keyword arguments
introduce(name="Alice", age=30, city="New York")
#name: Alice
# age: 30
# city: New York


# 9. *Explain the concept of function scope in Python.*
#    - *Answer:* Function scope in Python defines the visibility of variables within functions. Variables defined inside a function are local to that function by default and cannot be accessed from outside unless declared global or nonlocal.

# 10. *What is a lambda function in Python? When should it be used?*
#     - *Answer:* A lambda function is a small anonymous function defined using the lambda keyword. It can have any number of arguments but only one expression. Lambda functions are used when a simple function is needed for a short period of time.

# 11. *How are functions passed as arguments to other functions in Python?*
#     - *Answer:* In Python, functions are first-class objects, meaning they can be passed as arguments to other functions. This is commonly used in functional programming and callback mechanisms.

# 12. *What is a docstring in Python, and why is it used?*
#     - *Answer:* A docstring in Python is a string literal used to describe a function, module, or class. It is placed immediately after the function definition's header and is used to document what the function does, its parameters, and return value.

# In Python, a docstring is a string that is used to document a specific module, class, method, or function. It helps others understand what your code does. You define a docstring right below the function, class, or method definition. A docstring is written using triple quotes `"""` so that it can span multiple lines.
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The sum of the two numbers
    """
    return a + b

# Calling the function
result = add_numbers(3, 5)
print(result)  # Output: 8
# - You can access the docstring using the `help()` function or by using `__doc__`.
# print(add_numbers.__doc__)

# 13. *Explain recursion in Python with an example.*
# Recursion in Python is a technique where a function calls itself directly or indirectly. Example of a recursive function to calculate factorial:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
      
# 14. *What are decorators in Python? How do they work with functions?*
#     - *Answer:* Decorators in Python are a powerful way to modify the behavior of functions or methods without changing their code directly. They are defined using the @decorator_function syntax and can be used to add functionality such as logging, timing, or authentication to functions.

# 15. *Discuss the concept of closures in Python.*
#     - *Answer:* A closure in Python is a nested function that has access to variables in its enclosing scope even after the outer function has finished execution. Closures are created by defining a nested function and returning it or passing it as an argument.

# 16. **Explain the use of global and nonlocal keywords in Python functions.**
#     - *Answer:* global is used inside a function to declare that a variable refers to a global variable, not a local one. nonlocal is used inside a nested function to declare that a variable refers to a variable in the nearest enclosing scope other than the global scope.

# 17. *What are generator functions in Python? How are they different from regular functions?*
#     - *Answer:* Generator functions in Python use yield instead of return to produce a series of values lazily, one at a time, rather than computing them all at once and returning a list. They are memory efficient for iterating over large datasets.

# 18. *How can you create a function that returns multiple values in Python?*
#     - *Answer:* Python functions can return multiple values by returning a tuple, list, or dictionary. Example:
#       python
#       def coordinates():
#           return (10, 20)

#       x, y = coordinates()
      

# 19. *Explain how you can define a function with optional arguments in Python.*
#     - *Answer:* Optional arguments in Python functions are specified by giving them a default value in the function definition. Example:
#       python
#       def greet(name, greeting="Hello"):
#           print(f"{greeting}, {name}!")

#Optional arguments in Python functions are parameters that have default values. When you define a function with optional arguments, you provide a default value for those arguments. If the caller of the function does not provide a value for these arguments, the default value is used.
def greet(name, age=25, city="Unknown"):
    print(f"Hello, {name}! You are {age} years old and live in {city}.")

# Calling the function without optional arguments
greet("Alice")

# Calling the function with one optional argument
greet("Bob", 30)

# Calling the function with all arguments
greet("Charlie", 35, "New York")
# Hello, Alice! You are 25 years old and live in Unknown.
# Hello, Bob! You are 30 years old and live in Unknown.
# Hello, Charlie! You are 35 years old and live in New York.

      

# 20. **Discuss the difference between def and lambda in Python functions.**
#     - *Answer:* def is used to define named functions with a block of code and a return statement, suitable for more complex operations. lambda is used to create anonymous functions with a single expression, often used for short, simple tasks.

# These questions and answers cover a range of topics related to function definition and function calling in Python, from basic syntax to more advanced concepts like closures and decorators.

