#1] # What is comprehension?
#==> Comprehension in Python refers to a concise way of creating data structures like lists, dictionaries, and sets. It allows you to construct these data structures using a more readable and expressive syntax compared to traditional methods such as loops and append() statements.

# Types of Comprehensions in Python:
# List Comprehension:***********************

# Used to create a new list by applying an expression to each item in an iterable.
# Syntax: [expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
print(squares)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# This creates a list of squares of numbers from 0 to 9.


# Dictionary Comprehension:
# Similar to list comprehension but creates dictionaries.
# Syntax: {key_exp: value_exp for item in iterable if condition}

square_dict = {x: x**2 for x in range(5)}
print(square_dict)#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# This creates a dictionary where keys are numbers and values are their squares.

# Set Comprehension:
# Similar to list comprehension but creates sets.
# Syntax: {expression for item in iterable if condition}

square_set = {x**2 for x in range(10)}
print(square_set)#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# This creates a set of squares of numbers from 0 to 9.

# Advantages of Comprehensions:
# Readability: Comprehensions provide a more readable and compact syntax compared to traditional loops.
# Performance: They are generally faster than traditional loops due to optimized implementation in Python.
# When to Use Comprehensions:
# Use comprehensions when you need to create a new list, dictionary, or set by applying an operation to each element of an existing iterable.

# Example:
# Let's say you have a list of numbers and you want to create a new list containing only the even numbers squared:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]

# In summary, comprehension in Python provides a powerful and concise way to create lists, dictionaries, and sets based on existing iterables, making your code more readable and often more efficient.


# Here are 20 practical interview questions on comprehensions in Python, along with their answers:

# ### List Comprehensions
# 1. **Q**: Write a list comprehension to create a list of squares of the first 10 natural numbers.
print()
y=[x**2 for x in range(1, 11)]
print(y)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. **Q**: Create a list comprehension that filters out all the even numbers from 1 to 20.
y=[x for x in range(1, 21) if x % 2 != 0]
print(y)#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 3. **Q**: How do you create a list of tuples where each tuple is a pair of numbers (i, j) such that i is from 1 to 3 and j is from 1 to 2?
y=[(i, j) for i in range(1, 4) for j in range(1, 3)]
print(y)#[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# 4. **Q**: Use a list comprehension to flatten a list of lists(taking a list that contains other lists and turning it into a single flat list.): `[[1, 2], [3, 4], [5, 6]]`.
y=[item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]
print(y)#[1, 2, 3, 4, 5, 6]

# 5. **Q**: Create a list comprehension that generates a list of the lengths of each word in a given sentence.
sentence = "This is a test"
lengths = [len(word) for word in sentence.split()]
print(lengths)  # Output: [4, 2, 1, 4]

# ### Dictionary Comprehensions********************

# 6. **Q**: Write a dictionary comprehension to create a dictionary where keys are numbers from 1 to 5 and values are their cubes.
y={x: x**3 for x in range(1, 6)}
print(y)#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 7. **Q**: Convert a list of tuples `[(1, 'a'), (2, 'b'), (3, 'c')]` into a dictionary using a comprehension.
y={key: value for key, value in [(1, 'a'), (2, 'b'), (3, 'c')]}
print(y)#{1: 'a', 2: 'b', 3: 'c'}

# 8. **Q**: How do you create a dictionary comprehension that filters out items with keys greater than 2 from a given dictionary `{1: 'a', 2: 'b', 3: 'c', 4: 'd'}`?
y={k: v for k, v in {1: 'a', 2: 'b', 3: 'c', 4: 'd'}.items() if k <= 2}
print(y)#{1: 'a', 2: 'b'}

# 9. **Q**: Write a dictionary comprehension to swap the keys and values of the dictionary `{1: 'a', 2: 'b', 3: 'c'}`.
y={v: k for k, v in {1: 'a', 2: 'b', 3: 'c'}.items()}
print(y)#{'a': 1, 'b': 2, 'c': 3}

# 10. **Q**: Create a dictionary comprehension to count the frequency of each character in the string "banana".
y={char: "banana".count(char) for char in set("banana")}
print(y)#{'a': 3, 'b': 1, 'n': 2}

# ### Set Comprehensions

# 11. **Q**: How do you create a set comprehension to generate a set of squares of numbers from 1 to 10?
s={x**2 for x in range(1, 11)}
print(s)#{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# 12. **Q**: Use a set comprehension to create a set of unique characters in the string "abracadabra".
s={char for char in "abracadabra"}
print(s)#{'c', 'a', 'b', 'd', 'r'}

# 13. **Q**: Create a set comprehension to filter out all vowels from the string "hello world".
s={char for char in "hello world" if char not in 'aeiou'}
print(s)#{'h', 'r', 'l', 'd', ' ', 'w'}

# 14. **Q**: Write a set comprehension to get all the prime numbers between 1 and 30.
s={num for num in range(2, 31) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))}
print(s)#{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

# 15. **Q**: Generate a set of tuples (x, y) for x in range(3) and y in range(3), where x is not equal to y.
s={(x, y) for x in range(3) for y in range(3) if x != y}
print(s)#{(0, 1), (1, 2), (2, 1), (2, 0), (0, 2), (1, 0)}

# ### Nested Comprehensions
# 16. **Q**: Write a nested list comprehension to create a 3x3 matrix with values initialized to 0.
s=[[0 for _ in range(3)] for _ in range(3)]
print(s)#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 17. **Q**: Use a nested list comprehension to transpose a given matrix `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.
s=[[row[i] for row in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]] for i in range(3)]
print(s)#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 18. **Q**: Create a nested dictionary comprehension to generate a dictionary of dictionaries: `{i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}`.
s={i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(s)#{1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}

# 19. **Q**: How do you create a nested list comprehension to generate a list of lists containing the multiplication table up to 5x5?
s=[[i*j for j in range(1, 6)] for i in range(1, 6)]

# 20. **Q**: Use a nested list comprehension to generate a list of all possible sums of pairs `(i, j)` where i and j range from 1 to 3.
s=[i + j for i in range(1, 4) for j in range(1, 4)]
print(s)#[2, 3, 4, 3, 4, 5, 4, 5, 6]

# These questions cover a variety of comprehension techniques, providing a solid foundation for understanding and using comprehensions effectively in Python.