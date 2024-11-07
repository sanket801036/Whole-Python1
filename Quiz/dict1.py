"""
1) Which of the following methods can be used to add a new key-value pair to an existing dictionary?
add()
append()
insert()
update()
Correct Answer: 4
Sure, let's go through each option and explain why it can or cannot be used to add a new key-value pair to an existing dictionary in Python:

1. **add()**:
    - **Explanation**: The `add()` method is not a valid method for dictionaries. It is a method used with sets to add a single element.
    - **Example with a set**:
      
      my_set = {1, 2, 3}
      my_set.add(4)
      print(my_set)  # Output: {1, 2, 3, 4}
      
    - **Why not for dictionaries**: Dictionaries do not have an `add()` method. Attempting to use `add()` on a dictionary will result in an AttributeError.

2. **append()**:
    - **Explanation**: The `append()` method is used with lists to add a single element to the end of the list.
    - **Example with a list**:
      my_list = [1, 2, 3]
      my_list.append(4)
      print(my_list)  # Output: [1, 2, 3, 4]
    
    - **Why not for dictionaries**: Dictionaries do not have an `append()` method. Attempting to use `append()` on a dictionary will result in an AttributeError.

3. **insert()**:
    - **Explanation**: The `insert()` method is used with lists to insert an element at a specified position.
    - **Example with a list**:
      ```python
      my_list = [1, 2, 3]
      my_list.insert(1, 4)
      print(my_list)  # Output: [1, 4, 2, 3]
      ```
    - **Why not for dictionaries**: Dictionaries do not have an `insert()` method. Attempting to use `insert()` on a dictionary will result in an AttributeError.

4. **update()**:
    - **Explanation**: The `update()` method is used with dictionaries to update the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
    - **Example with a dictionary**:
      ```python
      my_dict = {'a': 1, 'b': 2}
      new_pair = {'c': 3}
      my_dict.update(new_pair)
      print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
      ```
    - **Why it works for dictionaries**: The `update()` method is designed to add or update key-value pairs in a dictionary. It can take another dictionary or an iterable of key-value pairs (such as a list of tuples) and update the original dictionary accordingly.

Additionally, dictionaries allow adding key-value pairs through direct assignment:

- **Direct assignment**:
  - **Explanation**: You can add a new key-value pair directly by assigning a value to a new key.
  - **Example**:
    ```python
    my_dict = {'a': 1, 'b': 2}
    my_dict['c'] = 3
    print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
    ```

So, from the options given, `update()` is the correct method to add a new key-value pair to an existing dictionary.

2) How can you remove a specific item (key-value pair) from a dictionary
remove(key)
discard(key)
pop(key)
All of the above
Your Answer: 3

1.
remove(key):
Explanation: The remove(key) method is used with sets to remove a specific element from the set. It raises a KeyError if the key is not found in the set.
Example with a set:
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
Why not for dictionaries: Dictionaries do not have a remove() method. Attempting to use remove() on a dictionary will result in an AttributeError.
2.
discard(key):
Explanation: The discard(key) method is used with sets to remove a specific element from the set. It does not raise an error if the key is not found in the set.
Example with a set:
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
Why not for dictionaries: Dictionaries do not have a discard() method. Attempting to use discard() on a dictionary will result in an AttributeError.
3.
pop(key):
Explanation: The pop(key) method is used with dictionaries to remove and return the value associated with the specified key. If the key is not found, it raises a KeyError.
Example with a dictionary:
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(my_dict)  # Output: {'b': 2}
print(value)  # Output: 1
Why it works for dictionaries: The pop() method is designed to remove a specific key-value pair from a dictionary. It can be used to remove and retrieve the value associated with a given key.

The option "All of the above" is incorrect because remove(key) and discard(key) are not applicable to dictionaries. Only pop(key) is a valid method for removing a specific item (key-value pair) from a dictionary.
C

3)Which of the following is the correct way to create an empty dictionary in Python?
my_dict = {}
my_dict = dict()
my_dict = {()}
my_dict = []




1) Which of the following methods returns a list of all the values in the dictionary?
values()
get_values()
get()
list_values()
Your Answer: 1
Correct Answer: 1

2) Which of the following is the correct way to create an empty dictionary in Python?
my_dict = {}
my_dict = dict()
my_dict = {()}
my_dict = []
Your Answer: 3
Correct Answer: 1

3) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.update({'d': 4})

print(my_dict)

{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'a': 1, 'b': 2, 'c': 3, 'd': None}
{'a': 1, 'b': 2, 'c': 3, 'd': '4'}
Your Answer: 3
Correct Answer: 2

4) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

new_dict = my_dict.copy()

my_dict['b'] = 4

print(new_dict)

{'a': 1, 'b': 2, 'c': 3}
{'b': 2, 'c': 3}
{'a': 1, 'b': 4, 'c': 3}
{'a': 1, 'b': 2, 'c': 3, 'b': 4}
Your Answer: 4
Correct Answer: 1

5) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(len(my_dict))

3
4
2
{'a': 1, 'b': 2, 'c': 3}
Your Answer: 4
Correct Answer: 1

6) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['b'] = 4

print(my_dict['b'])

1
2
3
4
Your Answer: 3
Correct Answer: 2

7) Which method returns a copy of the dictionary?
copy()
clone()
duplicate()
replicate()
Your Answer: 4
Correct Answer: 1

8) Which of the following methods can be used to add a new key-value pair to an existing dictionary?
add()
append()
insert()
update()
Your Answer: 4
Correct Answer: 4

9) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.pop('b')

print(my_dict)

{'a': 1, 'b': 2}
{'b': 2, 'c': 3}
{'a': 1, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
Your Answer: 3
Correct Answer: 3

10) What does the values() method return in a dictionary?
A list of all keys
A list of all values
A list of tuples containing key-value pairs
A list of dictionaries
Your Answer: 4
Correct Answer: 2

11) What happens when you try to add a duplicate key to a dictionary?
The new value overwrites the existing one
It raises a SyntaxError
It raises a ValueError
The dictionary becomes unordered
Your Answer: 3
Correct Answer: 1

12) What will be the output of the following code?
my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict["d"])

1
2
3
KeyError
Your Answer: 3
Correct Answer: 4

13) Which of the following methods returns a list of tuples containing the key-value pairs in the dictionary?
items()
get_items()
get()
list_items()
Your Answer: 3
Correct Answer: 1

14) How to access the value associated with the key 'x' in a dictionary my_dict?
my_dict[x]
my_dict.get('x')
my_dict['x']
All of the above
Your Answer: 4
Correct Answer: 3

15) How do you check if a key exists in a dictionary?
key in my_dict
my_dict.contains(key)
my_dict.exists(key)
key.exists(my_dict)
Your Answer: 4
Correct Answer: 1

16) How can you remove a specific item (key-value pair) from a dictionary
remove(key)
discard(key)
pop(key)
All of the above
Your Answer: 3
Correct Answer: 3

17) What is the output of len(my_dict) where my_dict = {'a': 1, 'b': 2, 'c': 3}?
3
2
6
7
Your Answer: 2
Correct Answer: 1

18) Which method removes all key-value pairs from a dictionary?
clear()
pop()
delete()
remove()
Your Answer: 2
Correct Answer: 1

19) What will my_dict.keys() return?
A list of all keys in the dictionary
A list of all values in the dictionary
A list of tuples containing key-value pairs
A dictionary of all keys
Your Answer: 3
Correct Answer: 1

20) What will be the output of the following code?
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict.get('b', 0))

1
2
3
0
Your Answer: 2
Correct Answer: 2

21) Which of the following methods returns a list of all the keys in the dictionary?
keys()
get_keys()
get()
list_keys()
Your Answer: 3
Correct Answer: 1

22) What will happen if you try to access a key that doesn't exist in a dictionary using my_dict['unknown']?
It will raise a KeyError
It will return None
It will return an empty dictionary
It will return False
Your Answer: 2
Correct Answer: 1

23) Which of the following is true about dictionaries in Python?
Dictionary keys must be unique
Dictionaries are immutable
Dictionaries can only store numeric values
Dictionary is comma separated value within [ ]
Your Answer: 3
Correct Answer: 1


"""