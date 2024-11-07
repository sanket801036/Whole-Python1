# 1. What is a decorator in Python, and how is it different from a higher-order function?
# The decorator in python allows you to add new functionality to an existing function without modifying it's structure.it's usually implemented as Higher order function .its simply take function as an argument and extends it's behaviour
# The main differnce beetween Higher order function and decorator is that decorator called like @decorator_name and HOF called directly
def decorator(func):
    def wrapper():
        print("Before the function call")
    return wrapper 
@decorator
def Say():
    print("Hello")
Say()

# 2. Can a decorator accept arguments? How would you implement that?

# 3. How can you ensure a decorator preserves the metadata of the original function?
# 4. How would you write a class-based decorator?
# 5. Can a decorator be applied to a class? How does it work?
# 6. What happens if a decorator is applied multiple times to the same function?
# 7. How would you use a decorator to log the execution time of a function?
# 8. Can you use decorators to control access to a function (e.g., for authentication purposes)?
# 9. Can decorators be used to cache the result of function calls? How would you implement it?
# 10. How would you implement a decorator that allows retrying a function if it raises an exception?
print("-------------------------------------------------------------------------------------------------------------")

























# Here are 10 tricky and challenging interview questions related to Python decorators, along with their answers:

### 1. What is a decorator in Python, and how is it different from a higher-order function?
# A decorator allows you to add new functionality to an existing function without modifying its structure. It's usually implemented as a higher-order function, which takes another function as an argument and extends its behavior.

# The main difference between a decorator and a higher-order function is that a decorator is applied using the `@decorator_name` syntax, making it more concise and readable, while a higher-order function is called directly.
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()  # Output will show additional prints before and after "Hello!"

### 2. Can a decorator accept arguments? How would you implement that?
# Yes, a decorator can accept arguments by creating a wrapper function inside another function. This allows you to pass arguments to the decorator.
def repeat(n):
    def decorator(func):
        def wrapper(*args, kwargs):
            for _ in range(n):
                func(*args, kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
# greet("Alice")  # "Hello, Alice!" will be printed 3 times
# Here, `repeat(n)` is a decorator that takes an argument `n`, and it calls the decorated function `n` times.

### 3. How can you ensure a decorator preserves the metadata of the original function?
# You can use the `functools.wraps` decorator from the `functools` module to preserve the original function's metadata, such as its name, docstring, etc.
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, kwargs):
        print("Before function call")
        result = func(*args, kwargs)
        print("After function call")
        return result
    return wrapper
@decorator
def say_hello():
    """This function says hello"""
    print("Hello!")
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: This function says hell

### 4. How would you write a class-based decorator?
# A class-based decorator is implemented by creating a class that has a `__call__` method. This method allows the class to be used like a function.
class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, kwargs):
        print("Before function call")
        result = self.func(*args, kwargs)
        print("After function call")
        return result
@Decorator
def say_hello():
    print("Hello!")
# say_hello()  # Output: prints before and after "Hello!"

### 5. Can a decorator be applied to a class? How does it work?
# Yes, decorators can be applied to classes. When applied to a class, the decorator gets the class as its argument and can modify or extend its behavior.
def decorator(cls):
    class NewClass(cls):
        def new_method(self):
            print("New method added")
    return NewClass
@decorator
class MyClass:
    def original_method(self):
        print("Original method")
obj = MyClass()
obj.original_method()  # Output: Original method
obj.new_method()       # Output: New method added

### 6. What happens if a decorator is applied multiple times to the same function?
# When multiple decorators are applied to the same function, they are executed in the order they are written, with the one closest to the function being executed first.
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        return func()
    return wrapper
def decorator2(func):
    def wrapper():
        print("Decorator 2")
        return func()
    return wrapper
@decorator1
@decorator2
def say_hello():
    print("Hello!")
say_hello()
# Output:
# Decorator 1
# Decorator 2
# Hello!
# The decorators are applied from the bottom up but executed from top to bottom.

### 7. How would you use a decorator to log the execution time of a function?
# You can use the `time` module in combination with a decorator to measure and log the execution time of a function.
import time
def time_logger(func):
    def wrapper(*args, kwargs):
        start_time = time.time()
        result = func(*args, kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@time_logger
def slow_function():
    time.sleep(2)
# slow_function()  # Output: slow_function took 2.000x second

### 8. Can you use decorators to control access to a function (e.g., for authentication purposes)?
# Yes, decorators are often used to control access to functions. You can wrap the function in logic that checks for authentication or other conditions before allowing the function to run.
def requires_login(func):
    def wrapper(user_logged_in, *args, kwargs):
        if user_logged_in:
            return func(*args, kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper
@requires_login
def view_dashboard():
    print("Welcome to the dashboard!")
# view_dashboard(True)   # Output: Welcome to the dashboard!
# view_dashboard(False)  # Output: Access denied. Please log in.

### 9. Can decorators be used to cache the result of function calls? How would you implement it?
# Yes, you can use decorators to implement caching by storing the results of previous function calls in a dictionary or using `functools.lru_cache`.
def cache(func):
    cache_store = {}
    def wrapper(n):
        if n in cache_store:
            return cache_store[n]
        result = func(n)
        cache_store[n] = result
        return result
    return wrapper
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))  # Output: 55 (with caching applied)

### 10. How would you implement a decorator that allows retrying a function if it raises an exception?
# You can implement a retry mechanism using a decorator that catches exceptions and retries the function a set number of times.
def retry(num_retries):
    def decorator(func):
        def wrapper(*args, kwargs):
            for _ in range(num_retries):
                try:
                    return func(*args, kwargs)
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying...")
            print("Max retries exceeded.")
        return wrapper
    return decorator

@retry(3)
def unstable_function():
    print("Attempting to run function")
    raise ValueError("Random failure")

# unstable_function()

# Here, the `unstable_function` will be retried 3 times before giving up.
# These questions are designed to test your understanding of how decorators work and their practical applications in Python.




