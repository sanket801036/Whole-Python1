### 1. Using `map` to Multiply Corresponding Elements of Two Lists
#    Question: Given two lists, `list1` and `list2`, write a function that returns a new list containing the product of corresponding elements from `list1` and `list2` using `map`.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
def multiply_lists(list1, list2):
    return list(map(lambda x,y:x*y,list1,list2))
print(multiply_lists(list1, list2))  # Output: [4, 10, 18]
# lambda arguments: expression
# add = lambda x, y: x + y
# print(add(2, 3))  # Output: 5


### 2. Filtering Even Numbers Using `filter`
#    Question: Write a function that takes a list of numbers and returns only the even numbers using the `filter` function.
numbers = [1, 2, 3, 4, 5, 6]
def filter_evens(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
print(filter_evens(numbers))  # Output: [2, 4, 6]

### 3. Using `reduce` to Compute the Product of a List
#    Question: Write a function that returns the product of all elements in a list using the `reduce` function.
from functools import reduce
numbers = [1, 2, 3, 4]
def product_of_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
print(product_of_list(numbers))  # Output: 24

### 4. Combining `map` and `filter`*********************************************
#    Question: Write a function that squares all even numbers in a list using `map` and `filter`.
numbers = [1, 2, 3, 4, 5, 6]
def square_evens(numbers):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(square_evens(numbers))  # Output: [4, 16, 36]

### 5. Using `map` to Flatten a List of Lists
#    Question: Write a function that takes a list of lists and returns a flattened list using `map`.
l = [[1, 2, 3], [4, 5], [6, 7]]
def flatten_list(l):
    return [item for sublist in l for item in sublist]
print(flatten_list(l))  # Output: [1, 2, 3, 4, 5, 6, 7]

### 6. Using `reduce` to Compute the Maximum Element
#    Question: Write a function that returns the maximum element from a list using `reduce`.
from functools import reduce
numbers = [5, 1, 8, 3, 9, 2]
def max_in_list(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)
print(max_in_list(numbers))  # Output: 9

### 7. Generating Fibonacci Sequence Using `map`
#    Question: Write a function that generates the first `n` Fibonacci numbers using `map`.
def fibo(n):
    l = [0, 1]
    list(map(lambda _: l.append(l[-1] + l[-2]), range(2, n)))
    return l[:n]
print(fibo(5))  # Output: [0, 1, 1, 2, 3]

## 8. Using `filter` to Extract Words Containing a Specific Letter
#    Question: Write a function that filters words from a list that contain a specific letter using `filter`.
l = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def filter(words, letter):
    return list(filter(lambda word: letter in word, words))
print(filter(words, 'a'))  # Output: ['apple', 'banana', 'date']

### 9. Using `map` to Normalize a List of Values
#    Question: Write a function that normalizes a list of numbers to a range of 0 to 1 using `map`.
l = [5, 10, 15, 20]
def norm(l):
    min_val, max_val = min(l), max(l)
    return list(map(lambda x: (x - min_val) / (max_val - min_val), l))
print(norm(l))                                 # Output: [0.0, 0.25, 0.5, 0.75]


### 10. Using `reduce` to Compute the GCD of a List
#    Question: Write a function that computes the greatest common divisor (GCD) of a list of numbers using `reduce`.
from functools import reduce
from math import gcd
numbers = [24, 36, 48]
def gcd_of_list(numbers):
    return reduce(gcd, numbers)
print(gcd_of_list(numbers))  # Output: 12


