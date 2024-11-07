# ### Interview Questions on List Methods
# 2. What does the `extend()` method do?
l=[1,2,3,4,5]
l.extend([11, 12])
print(l)#[1, 2, 3, 4, 5, 11, 12]

# 11. What is the difference between `sort()` and `sorted()`? 
# sort() modifies the original list in place, while sorted() returns a new sorted list
l = [20, 10, 15]
s = sorted(l)
print(s)  # Output: [10, 15, 20]

# 13. What does the `enumerate()` function do with a list?******************************************************************************
# Adds a counter to an iterable and returns it as an enumerate object.   
l = [10, 15, 20]
for i,v in enumerate(l):
    print(i,v)
#     # Output:
#     # 0 10
#     # 1 15
#     # 2 20

# 14. What is the `filter()` function used for with lists?    
l = [5, 10, 15, 20]
f = list(filter(lambda x: x > 10, l))
print(f)  # Output: [15, 20]

# 15. How do you use the `map()` function with a list?
#The map() function applies a given function to all items in an input list (or any iterable) and returns a map object (an iterator). This map object can be converted to a list or another iterable type.  
l = [1, 2, 3, 4]
m = list(map(lambda x: x*2, l))
print(m)  # Output: [2, 4, 6, 8]

# 16. How do you use the `zip()` function with lists? #  pass the iterables you want to combine as arguments.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 17. What does the `any()` function do with a list?     #  any() asks, "Is there at least one True thing in this list?" If yes, it says True. If not, it says False.  
my_list = [0, 1, 0, 0]
print(any(my_list))  # This will print True because there's a 1 (which is True)
# Example 1:
my_list = [0, 0, 0]
print(any(my_list))  # Output: False
# All items are 0 (which is considered False), so result is False.

# Example 2:
my_list = [0, 1, 0]
print(any(my_list))  # Output: True
# There's a 1 (which is considered True), so result is True.

# Example 3:
my_list = ['', '', '']
print(any(my_list))  # Output: False
# All items are empty strings (considered False).

# Example 4:
my_list = ['', 'Hello', '']
print(any(my_list))  # Output: True
# 'Hello' is a non-empty string (considered True).

# Example 5:
my_list = [False, False, True]
print(any(my_list))  # Output: True
# There's a True boolean value in the list.

# 18. What does the `all()` function do with a list?                # all() asks, "Are all the things in this list True?" If yes, it says True. If even one thing is False, it says False.
all_true = all([True, True, True])
print(all_true)  # Output: True

my_list = [1, 2, 3, 4]
print(all(my_list))  # This will print True because all numbers are non-zero (which are True)

my_list = [1, 0, 3, 4]
print(all(my_list))  # This will print False because 0 is considered False

# 19. How do you use list comprehensions?
# [expression for item in iterable if condition]

squared_list = [x**2 for x in range(10)]
print(squared_list)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# 20. How do you flatten a list of lists?    
l = [[1, 2], [3, 4], [5, 6]]
f = [j for i in l for j in i]
print(f)  # Output: [1, 2, 3, 4, 5, 6]

