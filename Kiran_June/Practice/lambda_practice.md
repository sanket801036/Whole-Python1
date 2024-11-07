# 1) What is a lambda function in Python and what is it used for?

Answer: A lambda function is a small anonymous function in  Python. It is defined using the "lambda" keyword and does not have a name. It is typically used for short, throwaway functions, such as for sorting or for applying a function to a list of elements.

# 2)How do you define a lambda function in  Python?

Answer: A lambda function is defined using the "lambda" keyword, followed by one or more arguments, a colon, and the function body.

For example:lambda x: x + 1

# 3)What is the difference between a lambda function and a regular Python function?

Answer: A lambda function is a small, anonymous function that does not have a name, whereas a regular  Python function is defined using the "def" keyword and has a name.  Lambda functions are also limited in functionality compared to regular functions, as they can only contain a single expression.

# 4)What is the syntax of a lambda function in  Python?

Answer: The syntax of a lambda function in Python is as follows:

lambda x: x*2
PythonCopy
# 5)How do you use a lambda function in Python?

Answer:  Lambda functions can be used in a variety of ways, including as arguments to other functions (such as the built-in "map" or "filter" functions), or to create short, throwaway functions for one-time use.

# 6)What are some examples of when you would use a lambda function in  Python?

Answer: Some examples of when you might use a lambda function in Python include:

Sorting a list of elements by a specific attribute
Applying a function to a list of elements
Creating a short, throwaway function for one-time use

# 7)What is the difference between a lambda function and a closure in  Python?

Answer: A lambda function is a small, anonymous function that does not have a name, whereas a closure is a function object that remembers values in the enclosing scope even if they are not present in memory.

# 8)How does a lambda function differ from a list comprehension in  Python?

Answer: A lambda function is a small, anonymous function that does not have a name, whereas a list comprehension is a more concise way to create a list in Python. While lambda functions can be used to perform operations on a list, list comprehensions are a more concise and readable way to perform those same operations.

# 9)Can a lambda function be used in place of a regular function in all cases in  Python?

Answer: No, lambda functions are limited in functionality compared to regular functions and are typically used for short, throwaway functions, so they can not be used in place of a regular function in all cases.

# 10)Are lambda functions slower than regular functions in  Python?

Answer: The performance of lambda functions is similar to that of regular functions in Python, so there should not be a noticeable difference in speed. However, as lambda functions are limited in functionality compared to regular functions, they may be slower in cases where they are used to perform more complex operations.

# 11)Can a lambda function have a return statement?

Answer: Yes, if it is a single expression function

# 12)What is the use of lambda function with filter() in  Python?

Answer: To filter out elements of a list that do not satisfy a certain condition.

# 13)When is it appropriate to use a lambda function in  Python?

Answer: When a function is going to be used only once.

# 14)Can a lambda function be defined inside a regular function in Python? -->

Answer: Yes, lambda functions can be defined inside regular functions in Python.

# 15)What is the difference between a lambda function and a generator expression in Python?

Answer: A lambda function is a small anonymous function while a generator expression creates an iterator.

# 16)What keyword is used to define a lambda function in  Python?

a) def
b) lambda
c) func
d) anonymous
Answer: b) lambda

# 17)How many expressions can a lambda function contain in  Python?

a) 1
b) 2
c) 3
d) Unlimited

Answer: a) 1

Explaination: A lambda function in Python can contain only one expression.

In lambda functions, the expression is automatically returned by the function, there is no need for a return statement.

# 18)Which of the following is a use case for a lambda function in Python?

a) Sorting a list of elements
b) Creating a user interface
c) Defining a class
d) Opening a file

Answer: a) Sorting a list of elements

# 19)What type of function is a lambda function in  Python?

a) Anonymous
b) Named
c) Both
d) None of the above

Answer: a) Anonymous

Explaination: A lambda function in  Python is an anonymous function, meaning it is a function without a name. It is defined using the "lambda" keyword, followed by one or more arguments and an expression.  Lambda functions are typically used as arguments to other functions, such as the built-in "map()" and "filter()" functions, and can be used to create small, one-time-use functions.

# 20)What built-in function in Python can take a lambda function as an argument?

a) print()
b) map()
c) open()
d) sorted()

Answer: b) map()

Explaination: The built-in function "map()" in  Python can take a lambda function as an argument. The "map()" function applies a given function to each item of an iterable (such as a list, tuple, or string) and returns an iterator that yields the results.

Code snippet:

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))
PythonCopy
# 21)What is the difference between a lambda function and a closure in  Python?

a) A lambda function is a small anonymous function while a closure is a function object that remembers values in the enclosing scope
b) A closure is a small anonymous function while a lambda function is a function object that remembers values in the enclosing scope
c) Both are the same
d) None of the above

Answer: a) A lambda function is a small anonymous function while a closure is a function object that remembers values in the enclosing scope

Explaination: A lambda function in  Python is a small, anonymous function defined using the "lambda" keyword. It can have one or more arguments and an expression and is often used as an argument to other functions such as the built-in "map()" and "filter()" functions.

A closure, on the other hand, is a function object that remembers values in the enclosing scope, even if they are not present in memory. A closure function is a nested function which has access to a free variable from its containing function that has finished its execution. Closures are used in cases where a function has to remember some state, such as in decorators or implementing a state machine.

Code Snippet:

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))
PythonCopy
# 22)How does a lambda function differ from a list comprehension in  Python?

a) A lambda function is a small anonymous function while a list comprehension is a more concise way to create a list
b) A list comprehension is a small anonymous function while a lambda function is a more concise way to create a list
c) Both are the same
d) None of the above

Answer: a) A lambda function is a small anonymous function while a list comprehension is a more concise way to create a list

# 23)Can a lambda function have a return statement?

a) Yes
b) No
c) Only if it's a single expression
d) It depends

Answer: c) Only if it's a single expression

Explaination: A lambda function in  Python can have a return statement, but only if it is a single expression. This means that the lambda function can only consist of one expression, and not multiple statements.
The expression of the lambda function is automatically returned by the function, thus the return statement is not necessary.

# 24)How to pass multiple arguments to a lambda function in  Python?

a) Using commas
b) Using semicolons
c) Using colons
d) Using parentheses

Answer: a) Using commas

Explaination: Multiple arguments can be passed to a lambda function in Python by using commas to separate them.
The arguments are listed after the lambda keyword, and the syntax is similar to that of a regular function definition.

Code Snippet :

lambda lst, key, value: [dict(i, **{key: value}) for i in lst]
PythonCopy
# 25)When is it appropriate to use a lambda function in  Python?

a) When a function is going to be used only once
b) When a function is going to be used multiple times
c) When a function is complex
d) When a function is simple

Answer: a) When a function is going to be used only once

Explaination: It is appropriate to use a lambda function in  Python when the function is going to be used only once. This is because lambda functions are anonymous, meaning they do not have a name and cannot be reused. They are typically used as arguments to other functions, such as the built-in "map()" and "filter()" functions, or as a quick way to define a small function for a specific task.

Code Snippet:

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
PythonCopy
# 26)What is the use of lambda function with map() in  Python?

a) To apply a certain function to all elements of a list
b) To filter out elements of a list that do not satisfy a certain condition
c) To sort a list of elements
d) To perform  mathematical operations on a list

Answer: a) To apply a certain function to all elements of a list

# 27)How can you use a lambda function to filter a list of integers?

Answer: Use the filter() function and pass the lambda function as the first argument, followed by the list of integers. The lambda function should return a Boolean value indicating whether the element should be included in the filtered list.

# 28)How can you use a lambda function to modify the values of a dictionary?

Answer: Use the map() function and pass the lambda function as the first argument, followed by the dictionary. The lambda function should take a key-value pair and return a modified key-value pair.

# 29)How can you use a lambda function to sort a list of strings alphabetically?


Answer: Use the sort() function and pass the lambda function as the key argument. The lambda function should take a string as an argument and return the string in lowercase.

# 30)How can you use a lambda function to calculate the sum of the elements in a list of integers?

Answer: Use the reduce() function from the functools module and pass the lambda function as the first argument, followed by the list of integers. The lambda function should take two arguments, the current total and the next element in the list, and return the updated total.

# 31)How can you use a lambda function to find the minimum value in a list of integers?

Answer: Use the min() function and pass the lambda function as the key argument, followed by the list of integers. The lambda function should take an integer as an argument and return the integer.

# 32)What are the limitations of lambda function in  Python?

Answer: 1) Limited Expressiveness:  Lambda functions are limited to a single expression and cannot contain statements or multiple expressions. This makes them less expressive and less powerful than traditional functions.

2)No Default Arguments:  Lambda functions do not support default arguments, which can make them less convenient to use in certain situations.

3)Limited Use Cases: Lambda functions are typically used for simple operations and are not well-suited for complex or large-scale tasks.

# 33)Write a program to find lambda function to multiply all elements in a list by a given number.


numbers = [1, 2, 3, 4, 5]

x = 2

result = list(map(lambda a: a*x, numbers))

print(result)
PythonCopy
Explanation:

1)The map() function is used to apply a specified function (in this case a lambda function) to each element of an iterable (in this case the list of numbers).

2)The lambda function takes a single argument a, which represents each element of the list, and multiplies it by x.

3)Then the list() function is used to convert the map object to a list and the result variable contains the final list of numbers after multiplying each element with the given number.

# 34)How do we use the  Lambda function in apply()?

Answer : The apply() function in  Pandas allows you to apply a function to a specific axis of a DataFrame. The function can be a built-in function, a user-defined function, or a lambda function.

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df['A'] = df.apply(lambda x: x['A'] ** 2, axis=1)

print(df)
PythonCopy
Explanation:

Here, we are using the apply() function to apply the lambda function on each row of the DataFrame (axis=1). The lambda function takes a single argument x, which represents each row of the DataFrame, and squares the value of the 'A' column (x['A'] ** 2).

The result is a new DataFrame with the squared values of the 'A' column.

# 35)When is it advised not to use a  Lambda function?

Answer: 1)When the logic is too complex:  Lambda functions are limited to a single expression, so if the logic is too complex or requires multiple expressions, it is best to use a regular function definition instead.

2)When the function needs to be reused: Since lambda functions are anonymous, they cannot be reused, so if the function needs to be reused in multiple places, it is best to use a regular function definition instead.

3)When the function requires default arguments: Lambda functions do not support default arguments, so if the function requires default arguments, it is best to use a regular function definition instead.

# 36)How is lambda assigned to a variable?

Answer: In  Python, a lambda function can be assigned to a variable just like any other value. This allows you to use the lambda function in multiple places, and also makes the code more readable.

squared = lambda x: x**2

print(squared(5)) # Output: 25
print(squared(10)) # Output: 100
PythonCopy
We are assigning the lambda function to a variable squared. Then we can use the variable squared as a function just like any other function. You can also pass the lambda function as an argument to other functions that accept a function as an argument, like map, filter, and reduce.

# 37)Is multithreading possible in lambda?

Answer :In  Python, it is possible to use multithreading with lambda functions, although it is not a very common use case. Multithreading allows you to run multiple threads concurrently, which can be useful for improving the performance of certain types of tasks.

When using multithreading with lambda functions, you should take into account the Global  Interpreter Lock (GIL) of  python, which is a mechanism used by the  interpreter to synchronize access to  Python objects.

# 38)What happens if a lambda function in python fails?

Answer :If a lambda function fails in Python, it will raise an exception just like any other function. The exception will be propagated to the calling code, and if it is not handled, it will cause the program to crash.

lambda_function = lambda: 1/0
try:
    lambda_function()
except ZeroDivisionError as e:
    print("An error occurred: ", e)
PythonCopy
It's important to note that since lambda functions are anonymous, it's harder to trace the origin of the error, thus it's recommended to add a comment or a meaningful name when defining the lambda function, to make it easier to debug.

# 39)Is  Lambda function in  python synchronous or asynchronous?

Answer: In  Python, a lambda function is synchronous, meaning that it runs in the same thread as the calling code and blocks the execution of the calling code until it completes.

A synchronous function runs in a linear fashion, it starts, runs to completion, and returns the result. While the calling code waits for the lambda function to complete, it cannot do any other work.

If you call a lambda function that performs a long-running task, such as a network call or a complex calculation, the calling code will be blocked until the lambda function completes.

# 40)How do you handle errors in lambda function in  python?

Answer : 1)Try-except block: You can use a try-except block to catch exceptions raised by the lambda function and handle them appropriately.

2)Return an error: You can return an error response from the lambda function, such as a tuple or a dictionary containing an error message and status code.

3)Use a logging library: You can use a logging library to log errors and exception raised by the lambda function, this way you can have a more detailed error message and track the error.

41)Can you use a lambda function with a decorator in  Python?

Answer: Yes, a lambda function can be used with a decorator in  Python. A decorator is a function that takes another function as its argument and extends the behavior of that function. In this case, the lambda function is passed as an argument to the decorator function, and the decorator function returns the lambda function with the added behavior.

# 42)How can you use a lambda function to find the intersection of two lists without using the set() or & operator?

Answer:

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = lambda x, y: [val for val in x if val in y]
print(intersection(list1, list2))
PythonCopy
The lambda function uses a list comprehension to iterate through the values in the first list and check if the value is also in the second list. The values that are present in both lists are added to a new list and returned.

# 43) How can you use a lambda function to find the Cartesian product of two lists without using itertools.product()?

Answer:

list1 = [1, 2, 3]
list2 = ['a', 'b']
cartesian_product = lambda x, y: [(a, b) for a in x for b in y]
print(cartesian_product(list1, list2))
PythonCopy
The lambda function uses a nested list comprehension to iterate through the values in the first list and the second list, and creates a tuple of each combination of values. The resulting list of tuples represents the Cartesian product of the two lists.

# 44)what is the difference between the filter and reduce function in  python lambdas?

Answer: The filter() function in  Python is used to filter a sequence (e.g. list, tuple, etc.) based on a certain condition, and return an iterator that only contains the elements that satisfy the condition.

The reduce() function in  Python is used to apply a binary function to a sequence in a cumulative way, so as to reduce the sequence to a single value.

The filter() function is used to filter elements from an iterable based on a given condition and the reduce() function is used to apply a binary operation to all elements in an iterable so as to reduce them to a single value.

# 45)How can a lambda function be used to sort a list of items?

a) list.sort(lambda x: x)
b) list.sort(key=lambda x: x)
c) list.sort(by=lambda x: x)
d) list.sort(func=lambda x: x)

Answer: b) list.sort(key=lambda x: x)

Explaination: A lambda function can be used to sort a list of items by passing it as the "key" argument to the built-in "sort()" method of a list.
The key argument is a function that takes one input and returns one output. This function is applied to each element of the iterable (list in this case) before sorting, and the returned values are used for sorting.

Code snippet:

words = ['foo', 'bar', 'baz', 'qux', 'quux']
words.sort(key=lambda x: len(x))
print(words)
PythonCopy
# 46)What is the correct syntax for defining a lambda function in  Python?

a) def lambda_func():
b) lambda:
c) lambda func:
d) def func():

Answer: b) lambda:

Explaination: The keyword lambda is used to define the function, followed by one or more arguments separated by commas. The arguments are followed by a colon (:) and the function's expression, which is evaluated and returned when the function is called.

Code Snippet:

lambda x, y: x + y
PythonCopy
# 47)What is the output of the following code?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
PythonCopy
a) [1, 3, 5, 7, 9]
b) [2, 4, 6, 8, 10]
c) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d) []

Answer: b) [2, 4, 6, 8, 10]

# 48)What is the output of the following code?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x * y, numbers)
print(result)
PythonCopy
a) 3628800
b) 0
c) 10
d) 55

Answer: a) 3628800

# 49)What is the main use of lambda functions in  Python?

a) To create anonymous functions that can be used only once
b) To define small, throwaway functions for specific tasks
c) To create complex, multi-line functions
d) To create reusable functions that can be used multiple times

Answer: b) To define small, throwaway functions for specific tasks

Explaination: The main use of lambda functions in  Python is to define small, throwaway functions for specific tasks. These functions are known as anonymous functions because they don't have a name.

They are used to perform a specific, often simple operation, and are typically passed as an argument to other functions, such as the built-in map() and filter() functions. They are often used to quickly define small functions for one-time use, without the need to define a separate, named function.

# 50)How can a lambda function be passed as an argument to the map() function?

a) map(lambda x: x * 2)
b) map(x: x * 2)
c) map(function(x) x * 2)
d) map(x => x * 2)

Answer: a) map(lambda x: x * 2)


Q1. What is a lambda function in Python?
a) A built-in function for performing mathematical calculations

b) A function that is defined with the def keyword

c) An anonymous function defined using the lambda keyword

d) A function that can only be used with strings

Answer: c


Explanation: Lambda functions in Python are anonymous functions defined with the lambda keyword.

Q2. Which of the following statements is true about lambda functions?
a) Lambda functions can have multiple expressions

b) Lambda functions can have default arguments

c) Lambda functions cannot have return statements

d) Lambda functions can be named and reused like regular functions

Answer: b

Explanation: Lambda functions can have default arguments, allowing flexibility in their usage.

Q3. What is the syntax for a lambda function in Python?
a) lambda arg1, arg2: expression

b) def lambda(arg1, arg2): expression

c) lambda function(arg1, arg2): expression

d) function(arg1, arg2): expression

Answer: a

Explanation: The syntax for a lambda function is lambda arguments: expression.

Q4. When are lambda functions typically used in Python?
a) To define large, complex functions

b) To create anonymous functions for simple tasks

c) To replace built-in functions like print() and input()

d) To handle exceptions in code

Answer: b

Explanation: Lambda functions are commonly used for creating small, anonymous functions for simple tasks.

Q5. Which of the following is a valid use case for a lambda function?
a) Sorting a list of tuples by the second element

b) Defining a class method

c) Handling file I/O operations

d) Performing matrix multiplication

Answer: a

Explanation: Lambda functions are often used for sorting, especially when the sorting key is based on a specific element in a tuple or object.

Q6. What is the output of the following code?
result = (lambda x: x * 2)(5)
print(result)
a) 5

b) 10

c) 25

d) 15

Answer: b

Explanation: The lambda function (lambda x: x * 2) multiplies the input 5 by 2, resulting in 10.

Q7. Which of the following is true about lambda functions?
a) They cannot have multiple parameters

b) They are always named

c) They can be used to create recursive functions

d) They can contain multiple lines of code

Answer: a

Explanation: Lambda functions are limited to a single expression, so they typically have a single parameter.

Q8. What is the purpose of using lambda functions with map() and filter() functions in Python?
a) To apply the lambda function to all elements of an iterable

b) To remove all elements from an iterable

c) To sort the elements of an iterable

d) To create a new iterable with selected elements

Answer: a

Explanation: Lambda functions are often used with map() and filter() to apply a function to all elements of an iterable and filter elements based on a condition, respectively.

Q9. What will be the output of the following code?
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, nums))
print(result)
a) [1, 2, 3, 4, 5]

b) [1, 4, 9, 16, 25]

c) [2, 4, 6, 8, 10]

d) [0, 1, 2, 3, 4]

Answer: b

Explanation: The map() function applies the lambda function to each element in nums, resulting in a new list with squared values.

Q10. What is the output of the following code?
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
a) [1, 3, 5]

b) [2, 4]

c) [1, 2, 3, 4, 5]

d) []

Answer: b

Explanation: The filter() function creates a new list with elements that satisfy the condition (even numbers) given by the lambda function.

Q11. What will the following code snippet output?
f = lambda x, y: x + y
result = f(2, 3)
print(result)
a) 2

b) 3

c) 5

d) 6

Answer: c

Explanation: The lambda function f adds its two arguments x and y, so f(2, 3) results in 2 + 3 = 5.

Q12. Which of the following is a correct lambda function to calculate the square of a number?
a) lambda x: x * x

b) lambda x: x ^ 2

c) lambda x: x ** 2

d) lambda x: x + x

Answer: c

Explanation: The lambda function lambda x: x ** 2 calculates the square of a number x.

Q13. What does the following lambda function do?
f = lambda x: x if x % 2 == 0 else None
result = f(5)
print(result)
a) Returns the number if it is even, otherwise None

b) Returns None if the number is even, otherwise the number

c) Returns the square of the number if it is even, otherwise None

d) Returns the number if it is odd, otherwise None

Answer: b

Explanation: The lambda function lambda x: x if x % 2 == 0 else None returns None if the input number x is even, otherwise it returns the number itself.

Q14. What will be the output of the following code?
greet = lambda: "Hello, World!"
result = greet()
print(result)
a) “Hello, World!”

b) “Hello!”

c) None

d) Error: lambda functions require arguments

Answer: a

Explanation: The lambda function greet has no arguments and returns the string “Hello, World!”, which is then printed.

Q15. What is the output of the following code?
func_list = [lambda x: x + 2, lambda x: x * 2, lambda x: x ** 2]
results = [func(5) for func in func_list]
print(results)
a) [7, 10, 25]

b) [10, 25, 7]

c) [7, 10, 5]

d) [10, 5, 25]

Answer: a

Explanation: Each lambda function in func_list is applied to the value 5, resulting in [5 + 2, 5 * 2, 5 ** 2].

Q16. Which of the following is a correct use of a lambda function with multiple arguments?
a) lambda x, y: x * y

b) lambda (x, y): x * y

c) lambda x y: x * y

d) lambda x: x * y

Answer: a

Explanation: The correct syntax for a lambda function with multiple arguments is lambda x, y: x * y.

Q17. What does the following lambda function do?
square_if_positive = lambda x: x ** 2 if x > 0 else None
result = square_if_positive(-3)
print(result)
a) Returns the square of a positive number, otherwise None

b) Returns None if the number is positive, otherwise the square of the number

c) Returns the square of the number if it is positive, otherwise None

d) Returns the number if it is positive, otherwise its square

Answer: c

Explanation: The lambda function square_if_positive returns the square of the number if it is positive, otherwise it returns None.

Q18. What is the output of the following code?
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x % 2 == 0, nums))
print(result)
a) [False, True, False, True, False]

b) [1, 0, 1, 0, 1]

c) [True, False, True, False, True]

d) [0, 1, 0, 1, 0]

Answer: a

Explanation: The map() function applies the lambda function to each element in nums, resulting in a list of Boolean values indicating whether each element is even.

Q19. Which of the following is a valid lambda function to check if a number is negative?
a) lambda x: x < 0

b) lambda x: x > 0

c) lambda x: x == 0

d) lambda x: x != 0

Answer: a

Explanation: The lambda function lambda x: x < 0 checks if a number is negative.

Q20. What will the following code snippet output?
f = lambda x: "even" if x % 2 == 0 else "odd"
result = f(7)
print(result)
a) “even”

b) “odd”

c) 7

d) None

Answer: b

Explanation: The lambda function f checks if a number is even or odd and returns the respective string.

Q21. What does the following lambda function do?
double_or_square = lambda x: x * 2 if x % 2 == 0 else x ** 2
result = double_or_square(3)
print(result)
a) Doubles the number if even, squares it if odd

b) Doubles the number if odd, squares it if even

c) Squares the number if even, doubles it if odd

d) Doubles the number if positive, squares it if negative

Answer: b

Explanation: The lambda function double_or_square doubles the number if it’s odd and squares it if it’s even.

Q22. What is the output of the following code?
students = ['Alice', 'Bob', 'Charlie', 'David']
sorted_students = sorted(students, key=lambda x: len(x))
print(sorted_students)
a) [‘Bob’, ‘Alice’, ‘David’, ‘Charlie’]

b) [‘Alice’, ‘Bob’, ‘Charlie’, ‘David’]

c) [‘David’, ‘Alice’, ‘Bob’, ‘Charlie’]

d) [‘Alice’, ‘Charlie’, ‘Bob’, ‘David’]

Answer: a

Explanation: The sorted() function sorts the list students based on the length of each name, resulting in [‘Bob’, ‘Alice’, ‘David’, ‘Charlie’].

Q23. What is the purpose of the lambda keyword in Python?
a) To define a regular function

b) To define a class method

c) To create anonymous functions

d) To create generator functions

Answer: c

Explanation: The lambda keyword is used to create anonymous functions, which are functions without a name.

Q24. Which of the following statements is true about lambda functions?
a) Lambda functions can contain multiple lines of code

b) Lambda functions can have docstrings

c) Lambda functions can be decorated

d) Lambda functions can use the yield keyword

Answer: b

Explanation: Lambda functions cannot have docstrings, as they are limited to a single expression.

Q25. What will the following code snippet output?
full_name = lambda first, last: f"{first.capitalize()} {last.capitalize()}"
result = full_name('john', 'doe')
print(result)
a) “John Doe”

b) “john doe”

c) “John doe”

d) “john Doe”

Answer: a

Explanation: The lambda function full_name capitalizes the first and last names and returns them as a full name.

Q26. Which of the following functions is equivalent to the lambda function lambda x: x ** 3?
a) def cube(x): return x * x * x

b) def cube(x): return x ** 2

c) def cube(x): return x * 3

d) def cube(x): return x + 3

Answer: a

Explanation: The lambda function lambda x: x ** 3 calculates the cube of x, which is equivalent to def cube(x): return x * x * x.

Q27. What will be the output of the following code?
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y
}

result_add = operations['add'](5, 3)
result_subtract = operations['subtract'](10, 4)
result_multiply = operations['multiply'](2, 6)

print(result_add, result_subtract, result_multiply)
a) 8 6 12

b) 3 6 12

c) 8 6 36

d) 3 6 36

Answer: a

Explanation: The dictionary operations contains lambda functions for addition, subtraction, and multiplication. The code then calls these functions with different arguments.

Q28. Which of the following is a correct lambda function to check if a number is prime?
a) lambda x: True if x % 2 == 0 else False

b) lambda x: True if x % 2 != 0 else False

c) lambda x: all(x % i != 0 for i in range(2, x))

d) lambda x: any(x % i == 0 for i in range(2, x))

Answer: c

Explanation: The lambda function lambda x: all(x % i != 0 for i in range(2, x)) checks if a number is prime by testing all numbers from 2 to x-1.

Q29. What is the output of the following code?
func = lambda x: x[1:]
result = func("Python")
print(result)
a) “ython”

b) “Python”

c) “P”

d) “y”

Answer: a

Explanation: The lambda function func returns the string x without its first character.

Q30. Which of the following is a correct lambda function to convert a string to uppercase?
a) lambda s: s.upper()

b) lambda s: s.capitalize()

c) lambda s: s.lower()

d) lambda s: s.title()

Answer: a

Explanation: The lambda function lambda s: s.upper() converts a string s to uppercase.

Q31. What does the following lambda function do?
add_two = lambda x, y: x + y
result = add_two(3, 4)
print(result)
a) Adds the two numbers

b) Multiplies the two numbers

c) Subtracts the second number from the first

d) Raises the first number to the power of the second

Answer: a

Explanation: The lambda function add_two adds its two arguments x and y, so add_two(3, 4) results in 3 + 4 = 7.

Q32. What will be the output of the following code?
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: x[-1])
print(sorted_names)
a) [“Charlie”, “David”, “Alice”, “Bob”]

b) [“Alice”, “David”, “Bob”, “Charlie”]

c) [“Bob”, “Alice”, “David”, “Charlie”]

d) [“Alice”, “Charlie”, “Bob”, “David”]

Answer: b

Explanation: The sorted() function sorts the list names based on the last character of each name, resulting in [“Alice”, “David”, “Bob”, “Charlie”].

# 81)Given a list of numbers, find all numbers divisible by 13.
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ] 
result = list(filter(lambda x: (x % 13 == 0), my_list))  
print(result)  
Output:
[65, 39, 221]
# 82)Given a list of strings, find all palindromes.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]  
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))  
#or
result = list(filter(lambda x: (x == x[::-1]), my_list))
print(result)  
Output :
['geeg', 'keek', 'aa']

# 83)Given a list of strings and a string str, print all anagrams of str
from collections import Counter 
  
my_list = ["geeks", "geeg", "keegs", "practice", "aa"] 
str = "eegsk"

result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list))  
  
print(result)  
Output :

['geeks', 'keegs']

def find_anagrams(string_list, target):
    sorted_target = sorted(target)
    anagrams = list(filter(lambda x: sorted(x) == sorted_target, string_list))
    for anagram in anagrams:
        print(anagram)
