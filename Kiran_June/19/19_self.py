# ### Questions on `return` Statement

# 1. **What is the purpose of the `return` statement in Python?**
   
#    **Answer:** The `return` statement is used to exit a function and go back to the place from where it was called. It can also return a value or multiple values from the function.

# 2. **What happens if there is no `return` statement in a function?**

#    **Answer:** If there is no `return` statement, the function will return `None` by default after executing all the statements in the function.

# 3. **Can a function return multiple values? If yes, how?**

#    **Answer:** Yes, a function can return multiple values by separating them with commas. These values are returned as a tuple.

def get_coordinates():
    x = 10
    y = 20
    return x, y

coords = get_coordinates()
print(coords)  # Output: (10, 20)

# 4. **What is the difference between `return` and `print`?**
#    **Answer:** `return` is used to send a result back from a function to its caller, while `print` is used to display output to the console. `return` affects the flow of the program, `print` does not.

# 5. **Can we use multiple `return` statements in a single function?**
#    **Answer:** Yes, a function can have multiple `return` statements, but only one will be executed, depending on the flow of the program.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(5))#Positive

# ### Questions on Nested Statements
# 1. **What is a nested statement in Python?**
#    **Answer:** A nested statement is a statement that is placed within another statement. For example, a nested loop is a loop inside another loop, and a nested function is a function defined inside another function.

# 2. **How do you write a nested `if` statement?**
#    **Answer:** A nested `if` statement is an `if` statement inside another `if` statement.
def check_value(x):
    if x > 0:
        if x % 2 == 0:
            return "Positive and even"
        else:
            return "Positive and odd"
    else:
        return "Non-positive"
print(check_value(9))# Positive and odd

# 3. **Can you provide an example of a nested loop?**
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print("=======")

#    i=0, j=0
#    i=0, j=1
#    i=1, j=0
#    i=1, j=1
#    i=2, j=0
#    i=2, j=1
#    ```

# 4. **What are the potential problems with nested loops?**

#    **Answer:** Nested loops can lead to increased time complexity, making the code less efficient. They can also make the code harder to read and maintain.

# 5. **How can you avoid deep nesting in your code?**
#    **Answer:** To avoid deep nesting, you can use early returns, break down complex functions into smaller ones, or use logical operators like `and`/`or` to combine conditions.

# ### Practical Example Questions
# 1. **Write a function that returns the factorial of a number using a nested function.**
def factorial(n):
    def inner_factorial(n):
        if n == 0:
            return 1
        else:
            return n * inner_factorial(n-1)
    return inner_factorial(n)  
print(factorial(5))
  # Output: 120

# 2. **Write a function that finds the maximum value in a 2D list (nested list).*****************************************************************************************************************
def find_max(matrix):
    max_value = float('-inf')
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value
   
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
   
print(find_max(matrix))  # Output: 9


# 3. **Write a function to check if a given number is prime using nested loops.**
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
   
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False

# These questions and examples should give you a solid understanding of how `return` statements and nested statements work in Python.