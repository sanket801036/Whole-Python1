# A decorator in Python is a function that wraps another function or method, adding some functionality to it without modifying its structure. Decorators are often used for logging, enforcing access control, instrumentation, or modifying behavior.

# ### Explanation
# Decorators allow you to modify the behavior of a function or method. They are commonly used in scenarios where you want to add functionality to an existing code in a reusable way.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()


# ### Output

# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# ### Explanation of the Example
# 1. Define a decorator function: `my_decorator` takes a function `func` as an argument and defines an inner function `wrapper`.
# 2. Wrapper Function: Inside the `wrapper` function, you can add any behavior you want before and after calling the original function `func`.
# 3. Return the Wrapper: The `my_decorator` function returns the `wrapper` function.
# 4. Apply the Decorator: The `@my_decorator` syntax is a shorthand for `say_hello = my_decorator(say_hello)`, meaning that `say_hello` is replaced with the `wrapper` function.

# This example demonstrates how you can use a decorator to add functionality (printing messages before and after the function call) to an existing function (`say_hello`) without modifying its code directly.





# Creating a decorator in Python involves defining a function that takes another function as an argument and returns a new function that adds some additional behavior. Here’s a step-by-step guide with a simple example:


# 1. Define the decorator function:
#    - This function will take another function as an argument.

# 2. Define a wrapper function inside the decorator:
#    - The wrapper function will add the new behavior.
#    - It will call the original function.

# 3. Return the wrapper function:
#    - The decorator function returns the wrapper function.

# Let’s create a simple decorator that prints a message before and after calling the decorated function.

# # Step 1: Define the decorator function
def my_decorator(func):
    # Step 2: Define the wrapper function
    def wrapper():
        print("Before the function is called.")
        func()  # Call the original function
        print("After the function is called.")
    # Step 3: Return the wrapper function
    return wrapper

# # Step 4: Use the decorator on a function
@my_decorator
def say_hello():
    print("Hello!")

# # Step 5: Call the decorated function
say_hello()


# ### Output

# Before the function is called.
# Hello!
# After the function is called.


# ### Explanation

# 1. Define the Decorator (`my_decorator`):
#    - `my_decorator` is a function that takes another function `func` as an argument.

# 2. Define the Wrapper (`wrapper`):
#    - Inside `my_decorator`, `wrapper` is defined.
#    - The `wrapper` function prints a message before and after calling `func`.

# 3. Return the Wrapper:
#    - `my_decorator` returns the `wrapper` function, which effectively wraps `func` with additional behavior.

# 4. Apply the Decorator:
#    - The `@my_decorator` syntax is used to decorate the `say_hello` function.
#    - This means `say_hello` is replaced with `my_decorator(say_hello)`, which is the `wrapper` function.

# 5. Call the Decorated Function:
#    - When `say_hello()` is called, it actually calls the `wrapper` function, which adds the new behavior (printing messages) and then calls the original `say_hello` function.



# Decorators in Python offer several advantages, making them a powerful tool for writing clean and efficient code. Here are some key benefits of using decorators:

# ### 1. Code Reusability
# - Advantage: Decorators allow you to reuse code across multiple functions without duplicating it.
# - Example: If you have several functions that need logging, you can write a logging decorator and apply it to each function instead of adding logging code to each one.

# ### 2. Separation of Concerns
# - Advantage: Decorators help separate the core functionality of a function from additional responsibilities like logging, access control, and performance monitoring.
# - Example: A function can focus solely on its main task while a decorator handles logging or access checks.

# ### 3. Enhanced Readability
# - Advantage: Decorators can make your code more readable by clearly indicating modifications to a function’s behavior.
# - Example: The `@staticmethod` or `@classmethod` decorators in Python make it clear that a method is static or a class method.

# ### 4. Flexibility and Extensibility
# - Advantage: You can easily extend the behavior of functions by chaining multiple decorators.
# - Example: You can use multiple decorators on a single function to add logging, caching, and access control, all at once.

# ### 5. Maintainability
# - Advantage: When functionality needs to change, you only have to update the decorator instead of modifying each function individually.
# - Example: If you need to change the logging format, you can update the logging decorator rather than updating every function that includes logging code.


# # A simple logging decorator
def log_decorator(func):
    def wrapper(*args, kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# # A function that performs addition
@log_decorator
def add(a, b):
    return a + b

# # Another function that performs multiplication
@log_decorator
def multiply(a, b):
    return a * b

# # Using the decorated functions
# add(2, 3)
multiply(4, 5)


# ### Output

# Calling add with arguments (2, 3) and {}
# add returned 5
# Calling multiply with arguments (4, 5) and {}
# multiply returned 20


# ### Explanation
# 1. Code Reusability: The `log_decorator` is used for both the `add` and `multiply` functions.
# 2. Separation of Concerns: The core logic of `add` and `multiply` is separate from logging.
# 3. Enhanced Readability: The `@log_decorator` clearly shows that logging is added to these functions.
# 4. Flexibility and Extensibility: Additional decorators can be added as needed.
# 5. Maintainability: Any changes to the logging behavior can be made in the `log_decorator` without touching the `add` and `multiply` functions.

# Decorators thus provide a clean, readable, and maintainable way to extend and modify the behavior of functions in Python.
