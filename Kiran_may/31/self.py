# ### 20 Questions on `set` Methods

# 1. What does the `add()` method do?

my_set = {1, 2}
my_set.add(3)
print(my_set)  # Output: {1, 2, 3}


# 2. What does the `remove()` method do?

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}


# 3. What does the `discard()` method do?
my_set = {1, 2, 3}
my_set.discard(4)  # No error if 4 is not present
print(my_set)  # Output: {1, 2, 3}


# 4. What does the `pop()` method do?
my_set = {1, 2, 3}
element = my_set.pop()  # Removes and returns an arbitrary element
print(element)
print(my_set)  # Output: Set without the removed element

# 5. What does the `clear()` method do?

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()


# 6. What does the `copy()` method do?

my_set = {1, 2, 3}
copied_set = my_set.copy()
print(copied_set)  # Output: {1, 2, 3}


# 7. What does the `union()` method do?

set1 = {1, 2}
set2 = {2, 3}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3}


# 8. What does the `intersection()` method do?

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}


# 9. What does the `difference()` method do?

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}

# 10. What does the `symmetric_difference()` method do?
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}

# 11. What does the `issubset()` method do?
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

# 12. What does the `issuperset()` method do?
set1 = {1, 2, 3}
set2 = { 1, 2}
print(set1.issuperset(set2))  # Output: True
 
# 13. What does the `isdisjoint()` method do?
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True
 

# 14. What does the `update()` method do?
my_set = {1, 2}
my_set.update([2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

# 15. What does the `intersection_update()` method do?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2) # Update a set with the intersection of itself and another
print(set1)  # Output: {3, 4}
 

# 16. What does the `difference_update()` method do?
 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2) # Remove all elements of another set from this set.
print(set1)  # Output: {1, 2}
 

# 17. What does the `symmetric_difference_update()` method do?
 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2) # Update a set with the symmetric difference of itself and another.
print(set1)  # Output: {1, 2, 4, 5}
 

# 18. What does the `add()` method return?
#     - The `add()` method does not return a value; it modifies the set in place.

# 19. What does the `pop()` method return?
#     - The `pop()` method returns the removed element from the set.

# 20. How do you use the `frozenset` constructor?
 
my_list = [1, 2, 3, 4]
my_frozenset = frozenset(my_list) # Build an immutable unordered collection of unique elements
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})
 

# These questions and answers cover various aspects of using sets and set methods in Python, from basic operations to more advanced methods.
