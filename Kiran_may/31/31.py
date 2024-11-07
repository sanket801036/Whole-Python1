# ### Removing Elements from a Set

# 1. Using `remove()` method:
# Removes the specified element from the set. Raises a `KeyError` if the element is not found.
s = {11, 22, 33}
s.remove(22)
print(s)
    #  {11, 33}

# 2. Using `discard()` method:
# Removes the specified element from the set. Does not raise an error if the element is not found.
t = {11, 22, 33}
t.discard(33)
print(t)
#      {11, 22}
 
# ### Intersection of Sets
# - Concept: The intersection of two sets is a set containing only the elements that are common to both sets.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s = s1.intersection(s2)
print(s)  # Output: {3, 4}`

# ### Difference of Sets
# 1. Difference of `s1` and `s2`:
# The difference of set `s1` and set `s2` is a set containing elements that are in `s1` but not in `s2`.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
d = s1.difference(s2)
print(d)  # Output: {1, 2}

# 2. Difference of `s1` and `s1`:
# The difference of a set with itself is an empty set, as there are no elements in `s1` that are not in `s1`.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
d = s1.difference(s1)
print(d)  # Output: set()

