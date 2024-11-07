Here are the answers to each of the questions you provided:

1. **Lambda Functions**
   - **Question:** Write a Python function using lambda that returns the square of a number if the number is even; otherwise, it returns the cube of the number.
   - **Answer:**
     ```python
     result = lambda x: x**2 if x % 2 == 0 else x**3
     ```
     - **Explanation:** This lambda function checks if `x` is even using the condition `x % 2 == 0`. If true, it returns `x**2` (the square of `x`); otherwise, it returns `x**3` (the cube of `x`).

2. **Map and Filter**
   - **Question:** Given a list of integers, use `map` to square all the even numbers and `filter` to remove all odd numbers from the list in a single line.
   - **Answer:**
     ```python
     result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
     ```
     - **Explanation:** The `filter` function is used to keep only even numbers (`x % 2 == 0`). Then, `map` applies a lambda function to square each of these even numbers.

3. **Reduce**
   - **Question:** Write a Python function using `reduce` to find the product of all elements in a list.
   - **Answer:**
     ```python
     from functools import reduce

     product = reduce(lambda x, y: x * y, numbers)
     ```
     - **Explanation:** `reduce` takes a binary function (`lambda x, y: x * y`) and applies it cumulatively to the elements of the list, resulting in the product of all elements.

4. **Closures**
   - **Question:** Create a closure in Python that captures a number and then returns a function that adds any given number to the captured number.
   - **Answer:**
     ```python
     def make_adder(x):
         def adder(y):
             return x + y
         return adder

     add_five = make_adder(5)
     result = add_five(10)  # result will be 15
     ```
     - **Explanation:** The `make_adder` function creates a closure by capturing the value of `x`. The inner function `adder` uses `x` and adds it to `y`, the argument passed to `adder`. This allows `make_adder` to return a function that always adds `x` to its input.

5. **Partial Functions**
   - **Question:** Use `functools.partial` to create a new function from an existing function that always multiplies a number by 10.
   - **Answer:**
     ```python
     from functools import partial

     def multiply(x, y):
         return x * y

     multiply_by_10 = partial(multiply, 10)
     result = multiply_by_10(5)  # result will be 50
     ```
     - **Explanation:** `functools.partial` creates a new function (`multiply_by_10`) by fixing the first argument of the `multiply` function to 10. This new function only requires one argument, which will be multiplied by 10.

6. **Comprehensions with Functions**
   - **Question:** Given a list of integers, write a list comprehension that applies a lambda function to double the numbers, but only if they are greater than 3.
   - **Answer:**
     ```python
     result = [x * 2 for x in numbers if x > 3]
     ```
     - **Explanation:** The list comprehension iterates over each number in `numbers`, doubles it using `x * 2`, but only if the number is greater than 3 (`if x > 3`).

7. **Decorators**
   - **Question:** Write a decorator that prints "Start" before calling the function and "End" after the function has been called.
   - **Answer:**
     ```python
     def decorator(func):
         def wrapper(*args, **kwargs):
             print("Start")
             result = func(*args, **kwargs)
             print("End")
             return result
         return wrapper

     @decorator
     def say_hello():
         print("Hello")

     say_hello()
     ```
     - **Explanation:** The `decorator` function wraps another function `func`. It prints "Start" before calling `func` and "End" after. The `@decorator` syntax applies this decorator to the `say_hello` function.

8. **Currying**
   - **Question:** Write a curried function that takes two arguments, `a` and `b`, and returns their product. The function should be defined in a way that allows calling it like `multiply(2)(3)`.
   - **Answer:**
     ```python
     def multiply(a):
         def inner(b):
             return a * b
         return inner

     result = multiply(2)(3)  # result will be 6
     ```
     - **Explanation:** The `multiply` function returns another function `inner` that takes `b` as an argument. This allows the function to be curried, so it can be called with one argument at a time like `multiply(2)(3)`.

9. **Function Composition**
   - **Question:** Implement a function composition in Python where `f(g(x))` is achieved using two lambda functions `f` and `g`.
   - **Answer:**
     ```python
     f = lambda x: x + 2
     g = lambda x: x * 3

     composed_function = lambda x: f(g(x))
     result = composed_function(4)  # result will be 14
     ```
     - **Explanation:** `f(g(x))` is composed by applying `g` first (multiplying by 3), and then applying `f` (adding 2) to the result of `g(x)`.

10. **Recursion with Functional Style**
    - **Question:** Write a recursive function using a functional style that computes the factorial of a number.
    - **Answer:**
      ```python
      factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
      result = factorial(5)  # result will be 120
      ```
      - **Explanation:** The lambda function `factorial` is defined recursively. It returns 1 if `n` is 0 (base case), otherwise it returns `n * factorial(n - 1)`, which computes the factorial by multiplying `n` by the factorial of `n - 1`.