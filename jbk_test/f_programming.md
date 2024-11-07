# 1) What is the output of the following code?
my_list = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)
 

[1, 3, 5]
[2, 4]
[1, 2, 3, 4, 5]
[2, 4, 6]
Your Answer: 2
Correct Answer: 2

# 2) Which of the following functions is used to reduce a list to a single value by applying a function cumulatively to the items of the list?
map()
filter()
reduce()
apply()
Your Answer: 3
Correct Answer: 3

# 3) What is recursion in functional programming?
A loop that runs indefinitely
A function that calls itself
A function that modifies its arguments
A function that has side effects
Your Answer: 1
Correct Answer: 2

# 4) What is the output of the following code?
def func(a, b=10, c=20):
    return a + b + c

result = func(5, c=15)
print(result)
 

30
25
45
50
Your Answer: 1
Correct Answer: 1

# 5) What is functional programming?
A programming paradigm that treats computation as the evaluation of mathematical functions
A programming paradigm that relies on changing state and mutable data
A programming paradigm that uses only loops and conditional statements
A programming paradigm that focuses on object-oriented programming
Your Answer: 2
Correct Answer: 1

# 6) In Python, what is a default argument?
An argument passed to a function when it is called
An argument used in the function definition to receive data
A value assigned to a parameter in the function definition
A value returned by a function
Your Answer: 3
Correct Answer: 3

# 7) What is the output of the following code?
def func(a, b=2, c=3):
    return a * b * c

result = func(2, c=4)
print(result)
 

12
16
24
32
Your Answer: 2
Correct Answer: 3

# 8) What is the output of the following code?
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(multiply, numbers)
print(result)
 

120
15
[1, 2, 3, 4, 5]
0
Your Answer: 1
Correct Answer: 1

# 9) Which of the following is NOT a benefit of using functional programming?
Simplicity
Easy parallelization
Mutable state
Predictability
Your Answer: 4
Correct Answer: 3

# 10) Which of the following Python libraries is commonly used for functional programming?
NumPy
Matplotlib
TensorFlow
PyTorch
Your Answer: 1
Correct Answer: 1

# 11) What does the lambda function do in Python?
Defines anonymous functions
Creates a tuple
Defines a generator
Creates a list comprehension
Your Answer: 1
Correct Answer: 1

# 12) What is the output of the following code?
from functools import partial

def power(x, y):
    return x ** y

square = partial(power, y=2)
print(square(5))
 

10
25
125
5
Your Answer: 2
Correct Answer: 2

13) What is the output of the following code?
15
120
[1, 3, 6, 10, 15]
0
Your Answer: 2
Correct Answer: 1

14) In Python, what are arguments?
Values passed to a function when it is called
Variables used in the function definition to receive data
Values returned by a function
Variables used in the function call to pass data
Your Answer: 3
Correct Answer: 1

15) What is currying in functional programming?
A technique to remove all the elements of a list
A technique to transform a function that takes multiple arguments into a chain of functions, each taking a single argument
A technique to add elements to a list
A technique to reverse the order of elements in a list
Your Answer: 2
Correct Answer: 2

16) What is the output of the following code?
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: add(x, 10), numbers))
print(result)
 

[1, 2, 3, 4, 5]
[10, 11, 12, 13, 14]
[11, 12, 13, 14, 15]
[20, 30, 40, 50, 60]
Your Answer: 2
Correct Answer: 3

17) Which of the following functions applies a function of two arguments cumulatively to the items of iterable, from left to right?
map()
filter()
reduce()
apply()
Your Answer: 4
Correct Answer: 3

18) Which of the following is NOT a higher-order function in Python?
map()
filter()
apply()
reduce()
Your Answer: 3
Correct Answer: 3

19) Which of the following higher-order functions applies a function to each element of a list and returns a new list with the results?
filter
reduce
map
flatMap
Your Answer: 2
Correct Answer: 3

20) What is the output of the following code?
def func(a, b, c):
    return a * b * c

result = func(c=3, b=2, a=1)
print(result)
 

5
6
9
12
Your Answer: 2
Correct Answer: 2

21) What does pure function mean in functional programming?
A function that modifies its arguments
A function that doesn't modify its arguments and has no side effects
A function that modifies global variables
A function that has side effects
Your Answer: 2
Correct Answer: 2

22) In Python, which of the following is true about parameters with default values?
hey must be specified in the function call
They must be specified in the function definition
They cannot be overridden in the function call
They can be overridden in the function call
Your Answer: 4
Correct Answer: 4

23) What is the output of the following code?
def greet(name, message='Hello'):
    print(f"{message}, {name}!")

greet("John")

Hello, John!
John, Hello!
Hello, world!
John, world!
Your Answer: 1
Correct Answer: 2

24) What is the main advantage of immutability in functional programming?
It makes debugging easier
It allows for easier implementation of parallel and concurrent programming
It improves the performance of the code
It allows the programmer to change the state of variables frequently
Your Answer: 2
Correct Answer: 2

25) In Python, what are parameters?
Values passed to a function when it is called
Variables used in the function definition to receive data
Values returned by a function
Variables used in the function call to pass data
Your Answer: 2
Correct Answer: 2

