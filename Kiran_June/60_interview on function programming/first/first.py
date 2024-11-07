# 1. Write a function that takes a list of numbers and returns a new list with each number squared
### Method 1: Using a For Loop
# This method uses a simple for loop to iterate through the list and append the squared values to a new list.
def square(num):
    sq = []
    for i in num:
        sq.append(i ** 2)
    return sq
num = [1, 2, 3, 4, 5]
print(square(num))
#[1, 4, 9, 16, 25]

### Method 2: Using List Comprehension
# List comprehension provides a concise way to create a new list by applying an expression to each element of the original list.
def sq(numbers):
    return [i**2 for i in num]
num = [1, 2, 3, 4, 5]
print(sq(num))
#[1, 4, 9, 16, 25]

### Method 3: Using the `map` Function
# The `map` function applies a given function to each item of an iterable (like a list) and returns a map object, which can be converted to a list.
def sq(num):
    return list(map(lambda x: x ** 2, num))
num = [1, 2, 3, 4, 5]
print(sq(num))
#[1, 4, 9, 16, 25]

# 2. Define a function that takes a string and returns the string reversed.
### Method 1: Using Slicing
def rev(s):
    return s[::-1]

### Method 2: Using a Loop
def rev(s):
    rev_str = ''
    for i in s:
        rev_str = i + rev_str
    return rev_str

### Method 3: Using the `reversed` Function and `join`
def rev(s):
    return ''.join(reversed(s))

### Method 4: Using Recursion
def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:]) + s[0]

### Method 5: Using Stack
def rev(s):
    stack = list(s)
    rev_string = ''
    while stack:
        rev_string += stack.pop()
    return rev

### Method 6: Using List Comprehension
def rev(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

# 3. How would you write a function to check if a number is a prime number?
### Basic Method
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(1))  # False
print("****")

### Optimized Method
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
print(is_prime(1))  # False

# ### Using a Helper Function
# def is_prime(n, divisor=2):
#     if n <= 1:
#         return False
#     if divisor * divisor > n:
#         return True
#     if n % divisor == 0:
#         return False
#     return is_prime(n, divisor + 1)
# def is_prime(n):
#     return is_prime(n)

# print(is_prime(17)) # True
# print(is_prime(18)) # False

### Using List Comprehension
def is_prime(n):
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))
print(is_prime(17)) # True
print(is_prime(18)) # False

### Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]

print(sieve_of_eratosthenes(10))  # [2, 3, 5, 7]
print(sieve_of_eratosthenes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]


print("#*******************************************4*******************************************************")
# 4. Implement a function that takes two strings and returns True if they are anagrams of each other.
# Anagrams are two strings that contain the same characters with the same frequency, but possibly in a different order.

### Method 1: Using a Dictionary to Count Characters
# **Concept**: Count the occurrences of each character in both strings and compare the counts.
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False 
    c = {}    
    for i in s1:
        c[i] = c.get(i, 0) + 1    
    for i in s2:
        if i not in c or c[i] == 0:
            return False
        c[i] -= 1    
    return all(value == 0 for value in c.values())
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

### Method 2: Using Sorting
# Sort both strings and compare them. If they are equal after sorting, they are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False


### Method 3: Using `collections.Counter`
# Use the `Counter` class from the `collections` module to count character occurrences and compare the counts.
from collections import Counter
def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False


### Method 4: Using a Fixed-Size Array
#  Use a fixed-size array to count character occurrences, assuming the input consists of only lowercase English letters.
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    c=[0]*26  # Assuming the strings contain only lowercase English letters   
    for i in s1:
        c[ord(i) - ord('a')] += 1    
    for i in s2:
        c[ord(i) - ord('a')] -= 1    
    return all(x == 0 for x in c)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False


### Method 5: XOR Approach
#  Use the XOR operation to compare characters. This method is less common and assumes that the strings are of equal length and consist of only lowercase English letters.
def are_anagrams(str1, str2):
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Initialize XOR result
    xor_result = 0
    
    # XOR all characters of both strings
    for char in str1:
        xor_result ^= ord(char)
    for char in str2:
        xor_result ^= ord(char)
    
    # If xor_result is 0, strings are anagrams
    return xor_result == 0

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False

print(are_anagrams("hello", "world"))    # False



# 5. Write a function that computes the factorial of a number using recursion.


# 6. Create a higher-order function that takes a function and a list, and applies the function to each element of the list.


# 7. Define a function that takes another function and an iterable, and returns a list of the results of applying the function to each element.


# 8. Write a lambda function to multiply two numbers.


# 9. Implement a function that takes a list of numbers and a threshold, and returns a list of numbers greater than the threshold using a lambda function.


# 10. Write a function that returns the Fibonacci sequence up to a given number n