# 1) What is the output of the following code?
def func(a, b, c):
    return a * b * c
result = func(c=3, b=2, a=1)
print(result)#6
 A 5
 B 6
 C 9
 D 12
Ans:- B
# 2) Which of the following is NOT a higher-order function in Python?
 A) map()
 B) filter()
 C) apply()
 D) reduce()
ans:C

# 3) In Python, what are arguments?
 A) Values passed to a function when it is called 
 B) Variables used in the function definition to receive data
 C) Values returned by a function
 D) Variables used in the function call to pass data
 Ans:-A

# 4) In Python, which of the following is true about parameters with default values?
 A) They must be specified in the function call
 B) They must be specified in the function definition
 C) They cannot be overridden in the function call
 D) They can be overridden in the function call
 Ans:-D

# 5) What is the output of the following code?

from functools import reduce
def multiply(x, y):
    return x * y
numbers = [1, 2, 3, 4, 5]
result = reduce(multiply, numbers)
print(result)

A120
B15
C[1, 2, 3, 4, 5]
D0
Ans:-A

# 6) What is recursion in functional programming?
A A loop that runs indefinitely
B A function that calls itself
C A function that modifies its arguments
D A function that has side effects
Ans:-(B) A function that calls itself

# 7) Which of the following is NOT a benefit of using functional programming?
A Simplicity
B Easy parallelization
C Mutable state
D Predictability
Ans:-C

# 8) Which of the following Python libraries is commonly used for functional programming?
A NumPy
B Matplotlib
C TensorFlow
D PyTorch
Ans:-A

# 9) What does pure function mean in functional programming?
A.A function that modifies its arguments
B.A function that doesn't modify its arguments and has no side effects
C.A function that modifies global variables
D.A function that has side effects
Ans:-B

# 10) What is the purpose of the functools module in Python?
A It provides tools for working with functions and callable objects
B It is used for creating GUI applications
C It is used for file I/O operations
D It is used for mathematical operations
Ans:-A

# 11) In Python, what is a default argument?
A An argument passed to a function when it is called
B An argument used in the function definition to receive data
C A value assigned to a parameter in the function definition
D A value returned by a function
Ans:-C

# 12) What is the main advantage of immutability in functional programming?
A It makes debugging easier
B It allows for easier implementation of parallel and concurrent programming
C It improves the performance of the code
D It allows the programmer to change the state of variables frequently
Ans:-B

# 13) What is the output of the following code?
def func(a, b=10, c=20):
    return a + b + c

result = func(5, c=15)
print(result)
 
A 30
B 25
C 45
D 50
Ans:-A

# 14) What is functional programming?
A A programming paradigm that treats computation as the evaluation of mathematical functions
B A programming paradigm that relies on changing state and mutable data
C A programming paradigm that uses only loops and conditional statements
D A programming paradigm that focuses on object-oriented programming
Ans:-A

# 15) What is the output of the following code?
def greet(name, message='Hello'):
    print(f"{message}, {name}!")

greet("John")

A Hello, John!
B John, Hello!
C Hello, world!
D John, world!
Ans:-A

# 16) In Python, which type of argument is passed by specifying the parameter name along with the value?
A Positional argument
B Default argument
C Keyword argument
D Arbitrary argument
Ans:-C

# 18) What does the lambda function do in Python?
A Defines anonymous functions
B Creates a tuple
C Defines a generator
D Creates a list comprehension
Ans:-A

# 19) Which of the following is a characteristic of functional programming?
A Mutable state
B Side effects
C Immutability
D Global variables
Ans:-C

# 20) What is the output of the following code?
from functools import partial

def power(x, y):
    return x ** y

square = partial(power, y=2)
print(square(5))
 

A 10
B 25
C 125
D 5

# 21) What is the output of the following code?
def func(a, b=2, c=3):
    return a * b * c

result = func(2, c=4)
print(result)
 

A12
B16
C24
D32
Ans:-B

# 22) What is the output of the following code?
my_list = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)
 

A[1, 3, 5]
B[2, 4]
C[1, 2, 3, 4, 5]
D[2, 4, 6]
Ans:- B

# 23) What is the output of the following code?
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: add(x, 10), numbers))
print(result)
 

A[1, 2, 3, 4, 5]
B[10, 11, 12, 13, 14]
C[11, 12, 13, 14, 15]
D[20, 30, 40, 50, 60]
Ans:-C

# 24) In Python, what is keyword argument?
A An argument passed to a function when it is called
B An argument used in the function definition to receive data
C a value assigned to a parameter in the function call using its name
D A value returned by a function
Ans:-C

# 25) Which of the following functions applies a function of two arguments cumulatively to the items of iterable, from left to right?
A map()
B filter()
C reduce()
D apply()
Ans:-C

1) What is the output of the following code?
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

2) Which of the following is NOT a higher-order function in Python?
map()
filter()
apply()
reduce()
Your Answer: 3
Correct Answer: 3

3) In Python, what are arguments?
Values passed to a function when it is called
Variables used in the function definition to receive data
Values returned by a function
Variables used in the function call to pass data
Your Answer: 1
Correct Answer: 1

4) In Python, which of the following is true about parameters with default values?
hey must be specified in the function call
They must be specified in the function definition
They cannot be overridden in the function call
They can be overridden in the function call
Your Answer: 4
Correct Answer: 4

5) What is the output of the following code?
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

6) What is recursion in functional programming?
A loop that runs indefinitely
A function that calls itself
A function that modifies its arguments
A function that has side effects
Your Answer: 2
Correct Answer: 2

7) Which of the following is NOT a benefit of using functional programming?
Simplicity
Easy parallelization
Mutable state
Predictability
Your Answer:
Correct Answer: 3

8) Which of the following Python libraries is commonly used for functional programming?
NumPy
Matplotlib
TensorFlow
PyTorch
Your Answer:
Correct Answer: 1

9) What does pure function mean in functional programming?
A function that modifies its arguments
A function that doesn't modify its arguments and has no side effects
A function that modifies global variables
A function that has side effects
Your Answer: 2
Correct Answer: 2

10) What is the purpose of the functools module in Python?
It provides tools for working with functions and callable objects
It is used for creating GUI applications
It is used for file I/O operations
It is used for mathematical operations
Your Answer: 1
Correct Answer: 1

11) In Python, what is a default argument?
An argument passed to a function when it is called
An argument used in the function definition to receive data
A value assigned to a parameter in the function definition
A value returned by a function
Your Answer:
Correct Answer: 3

12) What is the main advantage of immutability in functional programming?
It makes debugging easier
It allows for easier implementation of parallel and concurrent programming
It improves the performance of the code
It allows the programmer to change the state of variables frequently
Your Answer:
Correct Answer: 2

13) What is the output of the following code?
def func(a, b=10, c=20):
    return a + b + c

result = func(5, c=15)
print(result)
 

30
25
45
50
Your Answer:
Correct Answer: 1

14) What is functional programming?
A programming paradigm that treats computation as the evaluation of mathematical functions
A programming paradigm that relies on changing state and mutable data
A programming paradigm that uses only loops and conditional statements
A programming paradigm that focuses on object-oriented programming
Your Answer: 1
Correct Answer: 1

15) What is the output of the following code?
def greet(name, message='Hello'):
    print(f"{message}, {name}!")

greet("John")

Hello, John!
John, Hello!
Hello, world!
John, world!
Your Answer:
Correct Answer: 2

16) In Python, which type of argument is passed by specifying the parameter name along with the value?
 

Positional argument
Default argument
Keyword argument
Arbitrary argument
Your Answer: 3
Correct Answer: 3

17) What is the output of the following code?
15
120
[1, 3, 6, 10, 15]
0
Your Answer: 3
Correct Answer: 1

18) What does the lambda function do in Python?
Defines anonymous functions
Creates a tuple
Defines a generator
Creates a list comprehension
Your Answer: 1
Correct Answer: 1

19) Which of the following is a characteristic of functional programming?
Mutable state
Side effects
Immutability
Global variables
Your Answer: 3
Correct Answer: 3

20) What is the output of the following code?
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

21) What is the output of the following code?
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

22) What is the output of the following code?
my_list = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)
 

[1, 3, 5]
[2, 4]
[1, 2, 3, 4, 5]
[2, 4, 6]
Your Answer:
Correct Answer: 2

23) What is the output of the following code?
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: add(x, 10), numbers))
print(result)
 

[1, 2, 3, 4, 5]
[10, 11, 12, 13, 14]
[11, 12, 13, 14, 15]
[20, 30, 40, 50, 60]
Your Answer: 3
Correct Answer: 3

24) In Python, what is keyword argument?
An argument passed to a function when it is called
An argument used in the function definition to receive data
a value assigned to a parameter in the function call using its name
A value returned by a function
Your Answer: 3
Correct Answer: 3

25) Which of the following functions applies a function of two arguments cumulatively to the items of iterable, from left to right?
map()
filter()
reduce()
apply()
Your Answer: 3
Correct Answer: 3

