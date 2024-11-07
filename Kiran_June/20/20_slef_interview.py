
# ### Questions on Parameters and Arguments

# 1. **What is the difference between parameters and arguments in Python?**

#    **Answer:** Parameters are the variables listed inside the parentheses in the function definition, while arguments are the values passed to the function when it is called.


# def func(param1, param2):  # param1 and param2 are parameters
#     pass

# func(arg1, arg2)  # arg1 and arg2 are arguments


# 2. **What are default parameters?**

#    **Answer:** Default parameters are parameters that have a default value if no argument is provided during the function call.


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice

# 3. **What are keyword arguments?**

#    **Answer:** Keyword arguments are arguments passed to a function by explicitly stating the parameter name along with the value.


def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Good morning")  # Output: Good morning, Alice!

# 4. **What are *args and **kwargs?**

#    **Answer:** `*args` is used to pass a variable number of non-keyword arguments, while `**kwargs` is used to pass a variable number of keyword arguments.


def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, a=4, b=5)
   # Output:
   # (1, 2, 3)
   # {'a': 4, 'b': 5}


# 5.**Can you explain positional-only and keyword-only arguments?**

# In Python, you can specify that certain arguments in a function must be provided positionally or as keywords. This is useful for clarifying how a function should be called and can help prevent errors. 

### Positional-Only Arguments

# Positional-only arguments are specified using a / in the function signature. Any parameter before the / must be provided positionally.


def greet(name, /, greeting="Hello"):
    print(f"{greeting}, {name}!")

# # Correct usage
greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!

# # Incorrect usage
# greet(name="Alice")  # Raises a TypeError


# In this example, name must be passed positionally.

### Keyword-Only Arguments

# Keyword-only argum/ be provided positionally, and greeting must be provided as a keyword argument.
#Keyword-only arguments are specified using a * in the function signature. Any parameter after the * must be provided as a keyword argument.

# Example:

# def greet(*, name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# # Correct usage
# greet(name="Alice")  # Output: Hello, Alice!
# greet(name="Bob", greeting="Hi")  # Output: Hi, Bob!

# # Incorrect usage
# greet("Alice")  # Raises a TypeError


# In this example, name and greeting must be passed as keyword arguments.

### Combined Example

# You can combine both positional-only and keyword-only arguments in a single function:

# python
# def greet(name, /, *, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# # Correct usage
# greet("Alice")  # Output: Hello, Alice!
# greet("Bob", greeting="Hi")  # Output: Hi, Bob!

# # Incorrect usage
# greet(name="Alice")  # Raises a TypeError
# greet("Alice", "Hi")  # Raises a TypeError


# In this example, name must be provided positionally, and greeting must be provided as a keyword argument.


# ### Logical Questions

# 1. **How do you swap two variables in Python?**

#    **Answer:** You can swap two variables using tuple unpacking.

a, b = 1, 2
a, b = b, a
print(a, b)  # Output: 2, 1

# 2. **How do you check if a number is even or odd?**

def is_even(num):
    return num % 2 == 0
print(is_even(4))  # Output: True
print(is_even(3))  # Output: False


# 3. **How do you reverse a string in Python?**
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # Output: "olleh"


# 4. **How do you find the maximum value in a list?**
def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([1, 2, 3, 4, 5]))  # Output: 5


# 5. **How do you check if a string is a palindrome?**

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


# ### Practical Example Questions

# 1. **Write a function that takes a list of numbers and returns a new list with the square of each number.**


def square_numbers(numbers):
    return [num**2 for num in numbers]
print(square_numbers([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]


# 2. **Write a function that takes a string and returns a dictionary with the count of each character.**
def char_count(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

print(char_count("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# 3. **Write a function that takes a list and returns a new list with only the unique elements.**


def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]


# These questions and examples should provide a good understanding of parameters, arguments, and logical operations in Python.