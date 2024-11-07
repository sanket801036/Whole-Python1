# ### What is Exception Handling?
# Used to manage runtime errors. It ensures that the flow of the program can be maintained even in the presence of unexpected errors. By handling exceptions, you can prevent the program from crashing and provide more informative error messages to users.
# ### Purpose of Using `try` and `except` Block
# The try and except blocks are used to handle exceptions in Python:
# - try block:The code that might raise an exception is placed inside the `try` block.
# - except block: The code that runs if an exception occurs is placed inside the `except` block.
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ### What is the `raise` Statement?
# The `raise` statement is used to manually raise an exception in your code. This can be useful when you want to enforce certain conditions.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age
try:
    check_age(-2)
except ValueError as e:
    print(e)

# ### How to Create a User-Defined Exception Class
# In Python, you can create your own exception classes by inheriting from the built-in `Exception` class or any of its subclasses. This allows you to define custom behavior and attributes for your exceptions.
class NegativeAgeError(Exception):    
    def __init__(self, age, message="Age cannot be negative!"):
        self.age = age
        self.message = message
        super().__init__(self.message)
def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    return age
try:
    check_age(-2)
except NegativeAgeError as e:
    print(f"Error: {e.message} Age given: {e.age}")

# 1. A custom exception class `NegativeAgeError` is created, inheriting from the base `Exception` class.
# 2. The `__init__` method is overridden to accept an `age` parameter and a custom error message.
# 3. The `check_age` function raises a `NegativeAgeError` if the age is negative.
# 4. The `try` and `except` blocks handle the custom exception and print a custom error message.

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s). Please provide numbers.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

# Examples to show different scenarios
print("Example 1:")
divide_numbers(10, 2)  # No exception

print("\nExample 2:")
divide_numbers(10, 0)  # ZeroDivisionError

print("\nExample 3:")
divide_numbers(10, 'a')  # TypeError
