# ### Questions on Dictionary Methods
# 1.What does the `clear()` method do?**
#    - It removes all items from the dictionary:
#      my_dict.clear()

# 2.What does the `copy()` method do?**
#    - It returns a shallow copy of the dictionary:
#      dict_copy = my_dict.copy()

# 3.How does the `fromkeys()` method work?**
#    - It creates a new dictionary with specified keys and a default value:
#      new_dict = dict.fromkeys(['key1', 'key2'], 'default'

# 4.What is the purpose of the `get()` method?**
#    - It returns the value for the specified key if it exists, otherwise returns a default value:
#      value = my_dict.get('key', 'default_value')

# 5.How does the `items()` method work?**
#    - It returns a view object that displays a list of a dictionary’s key-value tuple pairs:
#      items = my_dict.items()

# 6.What does the `keys()` method return?**
#    - It returns a view object displaying a list of all the dictionary’s keys:
#      keys = my_dict.keys()

# 7.What does the `pop()` method do?**
#    - It removes the specified key and returns its value:
#      value = my_dict.pop('key')

# 8.How does the `popitem()` method work?**
#    - It removes and returns an arbitrary key-value pair (last item in Python 3.7+):

#      key, value = my_dict.popitem()
#      ```

# 9.What does the `setdefault()` method do?**
#    - It returns the value for the specified key if it exists, otherwise inserts the key with a default value and returns the default value:

# value = my_dict.setdefault('key', 'default')

# 10.How does the `update()` method work?**
#     - It updates the dictionary with elements from another dictionary or iterable of key-value pairs:

#       my_dict.update({'key3': 'value3'})


# 11.What is the difference between `pop()` and `popitem()`?**
#     - `pop()` requires a specific key and returns its value, while `popitem()` returns an arbitrary key-value pair (last item in Python 3.7+).

# 12.What does the `values()` method return?**
#     - It returns a view object that displays a list of all the dictionary’s values:

#       values = my_dict.values()


# 13.How can you use the `dict()` constructor to create a dictionary?**
#     - Use it with keyword arguments or an iterable of key-value pairs:
#       d1 = dict(key1='value1', key2='value2')
#       d2 = dict([('key1', 'value1'), ('key2', 'value2')])


# 14.How does the `dict.items()` method affect iteration?**
#     - It returns a view of the dictionary’s items, which you can iterate over:

#       for key, value in my_dict.items():
#           print(key, value)


# 15.What is the purpose of the `dict.setdefault()` method?**
#     - It returns the value for a key if it exists, otherwise inserts the key with a specified default value and returns the default value.

# 16.How can you use the `dict.update()` method to combine dictionaries?**
#     - Use `update()` to merge another dictionary into the current one:

#       my_dict.update(other_dict)


# 17.How can you retrieve a default value using `dict.get()`?**
#     - Provide a default value as the second argument to `get()`:
#       value = my_dict.get('key', 'default_value')

# 18.What is the significance of `dict.popitem()` in Python 3.7 and later?**
#     - It removes and returns the last key-value pair added, reflecting the insertion order.

# 19.What is the typical use case for the `dict.fromkeys()` method?*******************************************************************************************************
#     - To create a new dictionary with specified keys and a default value for all keys.

# 20.How can you use `dict.keys()` to check for the presence of a key?**
#     - Use the `in` operator with the `keys()` method:

#       if 'key' in my_dict.keys():
#           # key existsl


# These answers cover fundamental aspects of Python dictionaries and their operations, which should be useful for interview preparation.

