1) Which of the following methods returns a list of all the values in the dictionary?
values()
get_values()
get()
list_values()
Your Answer: 1
Correct Answer: 1

2) How to access the value associated with the key 'x' in a dictionary my_dict?
my_dict[x]
my_dict.get('x')
my_dict['x']
All of the above
Your Answer: 2
Correct Answer: 3

3) Which method returns a copy of the dictionary?
copy()
clone()
duplicate()
replicate()
Your Answer: 1
Correct Answer: 1

4) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['b'] = 4

print(my_dict['b'])

1
2
3
4
Your Answer: 4
Correct Answer: 2

5) Which of the following methods returns a list of tuples containing the key-value pairs in the dictionary?
items()
get_items()
get()
list_items()
Your Answer: 1
Correct Answer: 1

6) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.pop('b')

print(my_dict)

{'a': 1, 'b': 2}
{'b': 2, 'c': 3}
{'a': 1, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
Your Answer: 3
Correct Answer: 3

7) Which of the following is the correct way to create an empty dictionary in Python?
my_dict = {}
my_dict = dict()
my_dict = {()}
my_dict = []
Your Answer: 2
Correct Answer: 1

8) What happens when you try to add a duplicate key to a dictionary?
The new value overwrites the existing one
It raises a SyntaxError
It raises a ValueError
The dictionary becomes unordered
Your Answer: 1
Correct Answer: 1

9) What is the output of len(my_dict) where my_dict = {'a': 1, 'b': 2, 'c': 3}?
3
2
6
7
Your Answer: 1
Correct Answer: 1

10) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.update({'d': 4})

print(my_dict)

{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'a': 1, 'b': 2, 'c': 3, 'd': None}
{'a': 1, 'b': 2, 'c': 3, 'd': '4'}
Your Answer: 2
Correct Answer: 2

11) How can you remove a specific item (key-value pair) from a dictionary
remove(key)
discard(key)
pop(key)
All of the above
Your Answer: 4
Correct Answer: 3

12) What will my_dict.keys() return?
A list of all keys in the dictionary
A list of all values in the dictionary
A list of tuples containing key-value pairs
A dictionary of all keys
Your Answer: 4
Correct Answer: 1

13) Which of the following is true about dictionaries in Python?
Dictionary keys must be unique
Dictionaries are immutable
Dictionaries can only store numeric values
Dictionary is comma separated value within [ ]
Your Answer: 1
Correct Answer: 1

14) What will happen if you try to access a key that doesn't exist in a dictionary using my_dict['unknown']?
It will raise a KeyError
It will return None
It will return an empty dictionary
It will return False
Your Answer: 2
Correct Answer: 1

15) Which of the following methods returns a list of all the keys in the dictionary?
keys()
get_keys()
get()
list_keys()
Your Answer: 1
Correct Answer: 1

16) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict.get('b', 0))

1
2
3
0
Your Answer: 4
Correct Answer: 2

17) How do you check if a key exists in a dictionary?
key in my_dict
my_dict.contains(key)
my_dict.exists(key)
key.exists(my_dict)
Your Answer: 3
Correct Answer: 1

18) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

new_dict = my_dict.copy()

my_dict['b'] = 4

print(new_dict)

{'a': 1, 'b': 2, 'c': 3}
{'b': 2, 'c': 3}
{'a': 1, 'b': 4, 'c': 3}
{'a': 1, 'b': 2, 'c': 3, 'b': 4}
Your Answer: 1
Correct Answer: 1

19) Which of the following methods can be used to add a new key-value pair to an existing dictionary?
add()
append()
insert()
update()
Your Answer: 2
Correct Answer: 4

20) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(len(my_dict))

3
4
2
{'a': 1, 'b': 2, 'c': 3}
Your Answer: 1
Correct Answer: 1

21) Which method removes all key-value pairs from a dictionary?
clear()
pop()
delete()
remove()
Your Answer: 1
Correct Answer: 1

22) What does the values() method return in a dictionary?
A list of all keys
A list of all values
A list of tuples containing key-value pairs
A list of dictionaries
Your Answer: 2
Correct Answer: 2

23) What will be the output of the following code?
my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict["d"])

1
2
3
KeyError
Your Answer: 4
Correct Answer: 4

Let's go through each question and provide simple examples for each scenario:

1) **Which method returns a list of all the values in the dictionary?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.values())  # Output: dict_values([1, 2, 3])
```
2) **How to access the value associated with the key 'x' in a dictionary `my_dict`?**
```python
mydict = {'x': 5, 'y': 10}
print(my_dict['x'])  # Output: 5
```
3) **Which method returns a copy of the dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}
```

4) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['b'] = 4
print(my_dict['b'])  # Output: 4
```

5) **Which method returns a list of tuples containing the key-value pairs in the dictionary?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
```
6) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.pop('b')
print(my_dict)  # Output: {'a': 1, 'c': 3}
```

7) **Which of the following is the correct way to create an empty dictionary in Python?**
```python
my_dict = {}  # Correct way to create an empty dictionary
```
8) **What happens when you try to add a duplicate key to a dictionary?**
```python
my_dict = {'a': 1}
my_dict['a'] = 2
print(my_dict)  # Output: {'a': 2}  (The value of 'a' is updated)
```
9) **What is the output of `len(my_dict)` where `my_dict = {'a': 1, 'b': 2, 'c': 3}`?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3
```

10) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'d': 4})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
11) **How can you remove a specific item (key-value pair) from a dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
my_dict.pop('a')
print(my_dict)  # Output: {'b': 2}
```

12) **What will `my_dict.keys()` return?**
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])
```
13) **Which of the following is true about dictionaries in Python?**
```python
# Dictionary keys must be unique
my_dict = {'a': 1, 'b': 2, 'a': 3}  # The second 'a' will overwrite the first
print(my_dict)  # Output: {'a': 3, 'b': 2}
```

14) **What will happen if you try to access a key that doesn't exist in a dictionary using `my_dict['unknown']`?**
```python
my_dict = {'a': 1}
print(my_dict['unknown'])  # Raises KeyError
```

15) **Which method returns a list of all the keys in the dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])
```

16) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('b', 0))  # Output: 2
```

17) **How do you check if a key exists in a dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
print('b' in my_dict)  # Output: True
```

18) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()
my_dict['b'] = 4
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

19) **Which of the following methods can be used to add a new key-value pair to an existing dictionary?**
```python
my_dict = {'a': 1}
my_dict.update({'b': 2})
print(my_dict)  # Output: {'a': 1, 'b': 2}
```

20) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))
# Output: 3
```
21) **Which method removes all key-value pairs from a dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict)  # Output: {}

```
22) **What does the `values()` method return in a dictionary?**
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # Output: dict_values([1, 2])
```

23) **What will be the output of the following code?**
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['d'])  # Raises KeyError
```

These examples should give you a clear understanding of how the dictionary methods work in Python.