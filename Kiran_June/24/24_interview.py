# A lambda function in Python is a small anonymous function defined using the `lambda` keyword. Unlike regular functions defined using the `def` keyword, a lambda function is limited to a single expression. Here are the key characteristics and some examples of lambda functions:

# ### Characteristics of Lambda Functions

# 1. **Anonymous**: Lambda functions do not have a name.
# 2. **Single Expression**: Lambda functions can only contain one expression.
# 3. **Any Number of Arguments**: Lambda functions can take any number of arguments.
# 4. **Inline Definition**: Lambda functions are typically used for short, simple operations.

# The syntax of a lambda function is:

# lambda arguments: expression

# ### Examples
# 1. **Simple Lambda Function**:

square = lambda x: x**2
print(square(4))  # Output: 16

# 2. **Lambda Function with Multiple Arguments**:
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# 3. **Lambda Function Used with `map()`**:
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# 4. **Lambda Function Used with `filter()`**:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# 5. **Lambda Function Used with `sorted()`**:
data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# ### When to Use Lambda Functions
# - **Simple Functions**: Lambda functions are ideal for small, simple functions that are used only once or a few times.
# - **Inline Functions**: When you need a simple function for a short period of time, such as in functional programming constructs like `map()`, `filter()`, and `reduce()`.
# - **Sorting and Key Functions**: When providing a key function for sorting or other operations that require a callable.

# ### When Not to Use Lambda Functions
# - **Complex Functions**: For more complex functions with multiple statements, it's better to use a regular function defined with `def`.

# - **Readability**: If a lambda function's logic is complex enough to reduce readability, consider using a named function for clarity.

# ### Example of Regular Function vs. Lambda Function
# **Regular Function**:

# def add(x, y):
#     return x + y

# print(add(2, 3))  # Output: 5

# **Lambda Function**:
# add = lambda x, y: x + y
# print(add(2, 3))  # Output: 5


# In summary, lambda functions provide a concise way to create small, anonymous functions for short-term use, especially in functional programming contexts.



# Lambda functions in Python offer several advantages, particularly in contexts where concise and temporary function definitions are beneficial. Here are the key advantages:
# 1. **Conciseness**: Lambda functions allow for the definition of small functions in a single line, making the code more compact.
#    square = lambda x: x**2

# 2. **Readability**: For simple operations, lambda functions can make the code more readable by keeping the function definition close to its usage.
#    numbers = [1, 2, 3, 4]
#    squares = list(map(lambda x: x**2, numbers))

# 3. **No Need for Named Functions**: Lambda functions are ideal for cases where a function is used only once or for a short duration, avoiding the need to define a separate named function.

#    sorted_data = sorted(data, key=lambda x: x[1])

# 4. **Functional Programming**: Lambda functions are particularly useful in functional programming constructs like `map()`, `filter()`, and `reduce()`, where they can be used directly as arguments.
#    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 5. **Inline Definition**: They allow for inline function definitions, which can be handy for quick, throwaway functions.
# add = lambda x, y: x + y

# 6. **Anonymous Functions**: Lambda functions are anonymous, meaning they don't require a name, which can be beneficial for temporary functions used within another function or method.
#    def apply_func(f, x):
#        return f(x)
#    result = apply_func(lambda x: x + 2, 3)

# In summary, lambda functions are advantageous for creating small, concise, and temporary functions, especially in contexts where defining a full function with `def` would be cumbersome or unnecessary.
