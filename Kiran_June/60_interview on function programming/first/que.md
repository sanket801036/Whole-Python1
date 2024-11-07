### 1. Function Definition and Calling
**Definition**: A function is a block of organized, reusable code that performs a single. Functions provide better modularity for your application and a high degree of code reusability.

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

**Interview Questions**:
1. How do you define a function in Python?
2. What is the difference between a function and a method?
3. How can you return multiple values from a function?
4. Explain the importance of the `return` statement in a function.
5. Can a function call another function? Provide an example.

### 2. Global Scope and Local Scope
The scope of a variable determines the portion of the program where you can access a particular identifier. Variables declared outside a function are global, while variables declared inside a function are local.
x = "global"
def foo():
    x = "local"
    print(x)
foo()
print(x)

**Interview Questions**:
1. What is the difference between local and global variables?
2. How can you modify a global variable inside a function?
3. Explain the `global` keyword with an example.
4. What will happen if a variable has the same name in both local and global scopes?
5. How do you access a global variable from within a nested function?

### 3. Nested Function
 A function defined inside another function is called a nested function. It has access to the variables of the enclosing function.

def outer():
    x = "local"
    def inner():
        print(x)
    inner()
outer()

**Interview Questions**:
1. What is a nested function?
2. Explain the concept of closures with an example.
3. How can a nested function access variables from the outer function?
4. Can you return a nested function from an outer function? Provide an example.
5. How does the `nonlocal` keyword work in nested functions?

### 4. Arguments
 Functions can accept parameters/arguments to process data.

**Example**:
def add(a, b):
    return a + b
print(add(3, 4))

**Interview Questions**:
1. What are positional arguments?
2. Explain keyword arguments with an example.
3. What are default arguments? Provide an example.
4. How can you pass an arbitrary number of arguments to a function?
5. Explain the difference between `*args` and `**kwargs`.

### 5. Lambda Function
**Definition**: A lambda function is a small anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression.
**Example**:
add = lambda x, y: x + y
print(add(2, 3))

**Interview Questions**:
1. What is a lambda function?
2. How does a lambda function differ from a regular function?
3. Can you use lambda functions with higher-order functions? Provide an example.
4. What are some common use cases for lambda functions?
5. How can you write a lambda function with multiple lines of code?

### 6. Higher-Order Functions
**Definition**: Higher-order functions are functions that take other functions as arguments or return them as results.

**Example**:
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x * 2, 5))

**Interview Questions**:
1. What is a higher-order function?
2. Provide an example of a higher-order function.
3. Explain the concept of map, filter, and reduce functions.
4. How can you use the `sorted` function with a key argument as a lambda function?
5. Can a higher-order function return another function? Provide an example.

### Practical Interview Questions
1. Write a function that takes a list of numbers and returns a new list with each number squared.
2. Define a function that takes a string and returns the string reversed.
3. How would you write a function to check if a number is a prime number?
4. Implement a function that takes two strings and returns True if they are anagrams of each other.
5. Write a function that computes the factorial of a number using recursion.
6. Create a higher-order function that takes a function and a list, and applies the function to each element of the list.
7. Define a function that takes another function and an iterable, and returns a list of the results of applying the function to each element.
8. Write a lambda function to multiply two numbers.
9. Implement a function that takes a list of numbers and a threshold, and returns a list of numbers greater than the threshold using a lambda function.
10. Write a function that returns the Fibonacci sequence up to a given number n.
11. How can you use lambda functions with the `sorted` function to sort a list of dictionaries by a specific key?
12. Define a function that takes a list and a number, and returns a new list with each element multiplied by the number.
13. Write a function that merges two dictionaries into one.
14. Implement a nested function to calculate the power of a number.
15. How would you write a function to find the greatest common divisor (GCD) of two numbers?
16. Create a higher-order function that takes a list and a function, and applies the function to each element, returning a new list.
17. Define a function to flatten a nested list.
18. Write a function that removes duplicates from a list.
19. Implement a function that takes a list of numbers and returns the sum of all even numbers.
20. How can you use a lambda function with the `filter` function to filter out all negative numbers from a list?
21. Write a function that finds the longest word in a list of words.
22. Define a function that takes a list of integers and returns a list of their squares using a lambda function.
23. Implement a higher-order function that takes a function and two iterables, and returns a list of the results of applying the function to each pair of elements from the iterables.
24. Write a function that takes a string and returns a dictionary with the frequency count of each character.
25. How would you write a function to check if a string is a palindrome?
26. Create a lambda function that returns the maximum of two numbers.
27. Implement a function that takes a list of integers and returns a new list with only the odd numbers.
28. Define a function that returns the first n prime numbers.
29. Write a function that takes a list of numbers and returns the second largest number.
30. How can you use a lambda function with the `map` function to convert a list of strings to uppercase?
31. Implement a function that takes a string and returns True if all characters are unique.
32. Write a function that finds the intersection of two lists.
33. Define a function that takes a list of numbers and returns the average.
34. Implement a nested function to calculate the nth Fibonacci number.
35. How would you write a function to remove all whitespace from a string?
36. Create a lambda function to check if a number is even.
37. Write a function that returns the most frequent element in a list.
38. Define a function that takes a list of numbers and returns the cumulative sum.
39. Implement a function that takes a list of words and returns a list of words with more than three characters.
40. How can you use a lambda function with the `reduce` function to find the product of a list of numbers?
41. Write a function that takes a list of integers and returns a new list with each element incremented by one.
42. Define a function that takes a string and returns a list of all substrings.
43. Implement a function that takes a list of integers and returns the median.
44. How would you write a function to find the least common multiple (LCM) of two numbers?
45. Create a lambda function that returns the length of a string.
46. Write a function that removes all vowels from a string.
47. Define a function that takes a list of numbers and returns a list of their square roots.
48. Implement a function that takes a list of numbers and returns the sum of all odd numbers.
49. How can you use a lambda function with the `map` function to add two lists element-wise?
50. Write a function that takes a list of numbers and returns a new list with each number doubled.
51. Define a function that returns the number of words in a string.
52. Implement a function to find the common elements in three lists.
53. How would you write a function to generate all permutations of a list?
54. Create a lambda function that concatenates two strings.
55. Write a function that takes a list of tuples and returns a list of the first elements.
56. Define a function that takes a string and returns a new string with each word capitalized.
57. Implement a function that takes a list of numbers and returns the variance.
58. How can you use a lambda function with the `filter` function to filter out empty strings from a list?
59. Write a function that calculates the sum of digits of a number.
60. Define a function that takes a list of integers and returns a list of the prime numbers in the list.