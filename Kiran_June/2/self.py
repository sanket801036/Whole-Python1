# 1. Get all keys of a dictionary:

#    keys = d.keys()
#    # Output: dict_keys(['key1', 'key2', ...])


# 2. Get all values of a dictionary:

#    values = d.values()
#    # Output: dict_values(['value1', 'value2', ...])


# 3. Get all key-value pairs of a dictionary:

#    items = d.items()
#    # Output: dict_items([('key1', 'value1'), ('key2', 'value2'), ...])


# 4. Copy a dictionary:

#    dict_copy = d.copy()
#    # Output: A new dictionary with the same key-value pairs as d


# 5. Clear all items in a dictionary:
#    d.clear()
#    # Output: d is now {}

# 6. Use `setdefault()` method:
#    value = d.setdefault('key', 'default')
#    # Output: 'default' (if 'key' was not in d, it is now set to 'default')

# 7. `update()` method:
#    d.update({'key4': 'value4'})
#    # Output: d is updated with the new key-value pair

# 8. Sort a dictionary by keys or values:
#    sorted_by_key = dict(sorted(d.items()))
#    # Output: A new dictionary sorted by keys
   
#    sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
#    # Output: A new dictionary sorted by values

# 9. Find the number of items in a dictionary:
#    num_items = len(d)
#    # Output: Number of key-value pairs in d

# 10. Dictionary unpacking in function calls:
#     def func(a, b):
#         print(a, b)
#     params = {'a': 1, 'b': 2}
#     func(params)
#     # Output: 1 2

# 11. Remove all key-value pairs from a dictionary:
#     d.clear()
#     # Output: d is now {}
 
# 13. Use `pop()` method to remove and return a key-value pair:
#     value = d.pop('key1')
#     # Output: The value associated with 'key1'

# 14. Use `dict.fromkeys()` to create a new dictionary:
#     new_dict = dict.fromkeys(['key1', 'key2'], 'default_value')
#     # Output: {'key1': 'default_value', 'key2': 'default_value'}

# 15. Merge two dictionaries (Python 3.9+):

#     merged_dict = dict1 | dict2
#     # Output: A new dictionary containing key-value pairs from both dict1 and dict2
 

# 16. Perform a dictionary intersection:

#     intersected_dict = {k: dict1[k] for k in dict1 if k in dict2}
#     # Output: A dictionary with keys common to both dict1 and dict2
 

# 17. Dictionary addition (not supported directly):

#     combined_dict = {dict1, dict2}
#     # Output: A new dictionary combining dict1 and dict2
 

# 18. Filter a dictionary based on specific criteria:

#     filtered_dict = {k: v for k, v in d.items() if v > 10}
#     # Output: A new dictionary with key-value pairs where value > 10
 

# 19. Combine dictionaries with overlapping keys:

#     combined_dict = dict1.copy()
#     combined_dict.update(dict2)
#     # Output: combined_dict has keys from dict2 overwrite those in dict1
 

# 20. Check for equality between two dictionaries:

#     are_equal = dict1 == dict2
#     # Output: True if dict1 and dict2 are identical, False otherwise
 

lst = [10, 20, 10, 20, 30, 40]

s = []
c = []

for i in lst:
    if i % 2 == 0:
        s.append(i ** 2)
    else:
        c.append(i ** 3)

print(s)  # Squares of even numbers
print(c)  # Cubes of odd numbers