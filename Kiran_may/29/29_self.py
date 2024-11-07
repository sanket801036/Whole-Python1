# Certainly! Here are 20 practical interview questions with answers related to the `set` data structure in Python, followed by 20 questions specifically focused on `set` methods.

# ### 20 Logical Practical Interview Questions on `set`
# 1. How do you create a set in Python?
s = {1, 2, 3, 4}

# 2. What happens if you try to create a set with duplicate elements?
#    - Duplicates are automatically removed.
my_set = {1, 2, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# 3. How can you check if an element is in a set?
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True

# 4. How do you add an element to a set?
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# 5. How do you remove an element from a set?
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# 6. What happens if you try to remove an element that is not in the set using `remove()`?
#    - It raises a `KeyError`.
my_set = {1, 2, 3}
# my_set.remove(4)  # Raises KeyError

# 7. How do you remove an element from a set without raising an error if the element is not present?n
my_set = {1, 2, 3}
my_set.discard(4)  # No error if 4 is not present

# 8. How can you get the number of elements in a set?
my_set = {1, 2, 3}
print(len(my_set))  # Output: 3

# 9. How do you clear all elements from a set?
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# 10. How do you find the intersection of two sets?
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1 & set2
print(intersection)  # Output: {2, 3}
 
# 11. How do you find the union of two sets?   **************************************************************************************************
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print(union)  # Output: {1, 2, 3, 4, 5}

# 12. How do you find the difference between two sets?
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference = set1 - set2
print(difference)  # Output: {1}

# 13. How do you find the symmetric difference between two sets?
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff = set1 ^ set2
print(sym_diff)  # Output: {1, 2, 4, 5} # Return a set that contains all items from both sets, except items that are present in both sets:
# OR
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)   # Return the symmetric difference of two sets as a new set.
print(z)

# 14. How can you check if one set is a subset of another? 
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

# 15. How can you check if one set is a superset of another?
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
 
# 16. How do you create a set from a list?
l = [1, 2, 2, 3]
my_set = set(l)
print(my_set)  # Output: {1, 2, 3}
 
# 17. How do you check if two sets are disjoint?
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True
 

# 18. How do you copy a set?
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}
print("----------------------") 

# 19. What is a frozenset and how is it different from a regular set?
#     - A `frozenset` is an immutable version of a set. You cannot add or remove elements from a `frozenset`.
 
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})
 
# 20. How do you create a frozenset from a list? 
my_list = [1, 2, 2, 3]
my_frozenset = frozenset(my_list)
print(my_frozenset)  # Output:- frozenset({1, 2, 3})


