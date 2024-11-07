# Certainly! Here are 20 interview questions and answers on higher-order functions in Python, along with practical examples.

# ### Questions and Answers on Higher-Order Functions

# 1. **What is a higher-order function?**

#    **Answer:** A higher-order function is a function that can take other functions as arguments and/or return a function as its result.

def apply_func(f, x):
    return f(x)
print(apply_func(lambda x: x**2, 4))  # Output: 16


# 2. **Give an example of a higher-order function in Python.**

#    **Answer:** The `map()` function is a higher-order function as it takes a function and an iterable as arguments.


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]


# 3. **What is the `map()` function in Python?**
#    **Answer:** The `map()` function applies a given function to all items in an input list and returns an iterator.
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6]

# 4. **How does the `filter()` function work?**
#    **Answer:** The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


# 5. **Explain the `reduce()` function and give an example.**

#    **Answer:** The `reduce()` function applies a rolling computation to sequential pairs of values in a list. It is in the `functools` module.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# 6. **What is the difference between `map()` and `filter()`?**
#    **Answer:** `map()` applies a function to all items in an input list, whereas `filter()` applies a function to each item and returns only those items for which the function returns true.
# map() changes each element into something new.
# filter() picks only the elements that meet a condition.

# 7. **Can you use higher-order functions with custom functions?**

#    **Answer:** Yes, you can pass custom functions to higher-order functions like `map()`, `filter()`, and `reduce()`.
def add_one(x):
    return x + 1

numbers = [1, 2, 3]
incremented = list(map(add_one, numbers))
print(incremented)  # Output: [2, 3, 4]


# 8. **How do you use the `sorted()` function with a custom key function?**
#    **Answer:** The `sorted()` function can take a `key` argument, which is a function that extracts a comparison key from each list element.
data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)  # Output: [{'name': 'Jane', 'age': 20}, {'name': 'John', 'age': 25}]

# 9. **What is a callback function?**
#    **Answer:** A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

# 10. **Can you chain higher-order functions together?**
#     **Answer:** Yes, you can chain higher-order functions together.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: [4, 16]

# 11. **What is the `zip()` function and how can it be used with `map()`?**

#     **Answer:** The `zip()` function combines elements from multiple iterables into tuples. It can be used with `map()` to apply a function to pairs of elements from different iterables.

a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)  # Output: [5, 7, 9]

# 12. **How can you create a higher-order function that returns another function?**

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print(double(5))  # Output: 10


# 13. **What is the `functools.partial` function and how is it used?**
#     **Answer:** `functools.partial` is used to fix a certain number of arguments of a function and generate a new function.
from functools import partial
def power(base, exponent):
        return base ** exponent
square = partial(power, exponent=2)
print(square(4))  # Output: 16

# 14. **How do you use the `any()` and `all()` functions in Python?**
#     **Answer:** `any()` returns True if any element of the iterable is true, and `all()` returns True if all elements of the iterable are true.
numbers = [0, 1, 2, 3]
print(any(numbers))  # Output: True
print(all(numbers))  # Output: False

# 15. **How can higher-order functions improve code modularity?**
#     **Answer:** Higher-order functions can encapsulate behaviors and make the code more modular by separating concerns and promoting reuse of functions.

# 16. **Give an example of a higher-order function in a real-world scenario.**

#     **Answer:**
#     ```python
#     def apply_discount(price, discount_func):
#         return discount_func(price)

#     def ten_percent_off(price):
#         return price * 0.9

#     print(apply_discount(100, ten_percent_off))  # Output: 90.0
#     ```

# 17. **How do you use a lambda function inside a higher-order function?**

#     **Answer:** Lambda functions can be passed directly as arguments to higher-order functions.

#     numbers = [1, 2, 3]
#     incremented = list(map(lambda x: x + 1, numbers))
#     print(incremented)  # Output: [2, 3, 4]


# 18. **What is function composition and how can you achieve it with higher-order functions?**

#     **Answer:** Function composition is the process of combining two or more functions to produce a new function. You can achieve this by using higher-order functions.

#     ```python
#     def compose(f, g):
#         return lambda x: f(g(x))

#     def add_one(x):
#         return x + 1

#     def square(x):
#         return x**2

#     add_one_then_square = compose(square, add_one)
#     print(add_one_then_square(2))  # Output: 9
#     ```

# 19. **Explain how decorators are higher-order functions.**

#     **Answer:** Decorators are higher-order functions that take another function as an argument and extend or alter its behavior.

#     ```python
#     def my_decorator(func):
#         def wrapper():
#             print("Something is happening before the function is called.")
#             func()
#             print("Something is happening after the function is called.")
#         return wrapper

#     @my_decorator
#     def say_hello():
#         print("Hello!")

#     say_hello()
#     # Output:
#     # Something is happening before the function is called.
#     # Hello!
#     # Something is happening after the function is called.
#     ```

# 20. **How can higher-order functions be used for memoization?**

#     **Answer:** Higher-order functions can be used to create memoization decorators that cache results of expensive function calls.


#     def memoize(f):
#         cache = {}
#         def memoized_function(*args):
#             if args not in cache:
#                 cache[args] = f(*args)
#             return cache[args]
#         return memoized_function

#     @memoize
#     def fibonacci(n):
#         if n in [0, 1]:
#             return n
#         return fibonacci(n-1) + fibonacci(n-2)

#     print(fibonacci(10))  # Output: 55


# ### Practical Example Questions

# 1. **Write a higher-order function that applies a given function to each element in a list and returns a new list.
#     def apply_to_each(func, lst):
#         return [func(x) for x in lst]

#     result = apply_to_each(lambda x: x**2, [1, 2, 3, 4])
#     print(result)  # Output: [1, 4, 9, 16]


# 2. **Create a higher-order function that returns a function
#  to add a specific number to its argument.**

#     ```python
#     def make_adder(n):
#         return lambda x: x + n

#     add_five = make_adder(5)
#     print(add_five(10))  # Output: 15
#     ```

# 3. **Write a higher-order function that filters a list based on a given condition.**

#     ```python
#     def filter_list(condition, lst):
#         return [x for x in lst if condition(x)]

#     result = filter_list(lambda x: x > 2, [1, 2, 3, 4])
#     print(result)  # Output: [3, 4]
#     ```

# 4. **Use a higher-order function to sort a list of strings by their lengths.**

#     ```python
#     strings = ['apple', 'banana', 'cherry', 'date']
#     sorted_strings = sorted(strings, key=lambda s: len(s))
#     print(sorted_strings)  # Output: ['date', 'apple', 'banana', 'cherry']
#     ```

# 5. **Create a higher-order function that takes a function and an iterable, and returns a new iterable with the function applied to each element.**

#     ```python
#     def map_function(func, iterable):
#         return [func(x) for x in iterable]

#     result = map_function(lambda x: x * 2, [1, 2, 3])
#     print(result)  # Output: [2, 4, 6]
#     ```

# These questions and practical examples cover a wide range of concepts and applications of higher-order functions in Python, helping to demonstrate their versatility and power in functional programming.