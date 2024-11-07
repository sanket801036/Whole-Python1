### 1. How can you use list comprehension to flatten a nested list?
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
Explanation: The comprehension iterates over each sublist and each element inside the sublist.
### 2. How would you generate the Cartesian product of two lists using list comprehension?
A = [1, 2]
B = [3, 4]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
Explanation: Nested loops in list comprehension allow generating all possible combinations.

### 3. How do you create a list of even numbers from 0 to 50 using list comprehension?
evens = [x for x in range(51) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, ..., 50]
Explanation: The condition `x % 2 == 0` filters out only even numbers.

### 4. How can you use list comprehension to remove duplicates from a list?
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list({x for x in lst})
print(unique)  # Output: [1, 2, 3, 4, 5]
Explanation: Converting the list to a set removes duplicates, and list comprehension ensures it's converted back to a list.

### 5. How do you generate the transpose of a matrix using list comprehension?
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Explanation: The outer loop controls the column index, and the inner loop collects elements row-wise.
### 6. How can you reverse the elements of a list using list comprehension?
lst = [1, 2, 3, 4]
reversed_list = [lst[i] for i in range(len(lst)-1, -1, -1)]
print(reversed_list)  # Output: [4, 3, 2, 1]
Explanation: The comprehension iterates through the list indices in reverse.

### 7. How would you create a list of prime numbers within a given range using list comprehension?
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n0.5) + 1))
primes = [x for x in range(2, 50) if is_prime(x)]
print(primes)  # Output: [2, 3, 5, 7, 11, ..., 47]
Explanation: `is_prime` checks if a number is prime, and the list comprehension filters prime numbers.

### 8. How can you flatten a list of lists that may contain more nested lists (multiple levels of nesting)?
def flatten(lst):
    return [item for sublist in lst for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])]
nested_list = [1, [2, [3, 4], 5], 6]
flattened = flatten(nested_list)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
Explanation: A recursive function is used to handle deep nested lists.

### 9. How do you create a list of squares for all even numbers in a given range using list comprehension?
squares = [x2 for x in range(1, 20) if x % 2 == 0]
print(squares)  # Output: [4, 16, 36, 64, 100, 144, 196, 256, 324]
Explanation: The condition filters even numbers, and they are squared inside the comprehension.

### 10. How do you extract only the digits from a string using list comprehension?
s = "a1b2c3"
digits = [char for char in s if char.isdigit()]
print(digits)  # Output: ['1', '2', '3']
Explanation: The condition `char.isdigit()` selects only the numeric characters.
### 11. How do you generate a list of all palindromes in a range using list comprehension?
palindromes = [x for x in range(100, 200) if str(x) == str(x)[::-1]]
print(palindromes)  # Output: [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
Explanation: `str(x) == str(x)[::-1]` checks if the number is the same forwards and backwards.

### 12. How do you count the frequency of elements in a list using list comprehension?
lst = [1, 2, 2, 3, 3, 3]
freq = {x: lst.count(x) for x in set(lst)}
print(freq)  # Output: {1: 1, 2: 2, 3: 3}
Explanation: The comprehension creates a dictionary with counts of unique elements.

### 13. How can you generate a list of numbers divisible by 3 or 5 using list comprehension?
div_by_3_or_5 = [x for x in range(1, 50) if x % 3 == 0 or x % 5 == 0]
print(div_by_3_or_5)  # Output: [3, 5, 6, 9, 10, ..., 48]

### 14. How can you remove `None` values from a list using list comprehension?
lst = [1, None, 2, None, 3]
filtered = [x for x in lst if x is not None]
print(filtered)  # Output: [1, 2, 3]

### 15. How do you convert a list of strings to lowercase using list comprehension?
lst = ["HELLO", "WORLD"]
lowercased = [x.lower() for x in lst]
print(lowercased)  # Output: ['hello', 'world']

### 16. How do you generate the first 10 Fibonacci numbers using list comprehension?
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


### 17. How do you use list comprehension to remove negative numbers from a list?
lst = [1, -2, 3, -4, 5]
positive = [x for x in lst if x >= 0]
print(positive)  # Output: [1, 3, 5]

### 18. How can you transpose a 3x3 matrix diagonally using list comprehension?
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)  # Output: [1, 5, 9]

### 19. How do you generate a list of tuples where each tuple contains a number and its square?
tuples = [(x, x2) for x in range(1, 10)]
print(tuples)  # Output: [(1, 1), (2, 4), (3, 9), ..., (9, 81)]

### 20. How do you generate a list of all two-digit numbers with distinct digits using list comprehension?
distinct_digits = [10 * x + y for x in range(1, 10) for y in range(10) if x != y]
print(distinct_digits)  # Output: [12, 13, ..., 98]
