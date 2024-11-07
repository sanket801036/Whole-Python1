# "Pickling" is the process whereby a Python object is converted into a byte stream,
# "Unpickling" is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object 
# Pickling:-
# Pickling is also called as
# 1. Serialization
# 2. Marshalling
# 3. Flattening
# Important:
# 1. Pickled file has any extension
# 2. Picking: python object-->byte streams
# 3. Unpickling: Byte-streams python object
# 4. We have 'pickle' built-in module for this
# Disadvantages:
# 1. It is advisable not to unpickle data received from an untrusted source as they may have security threats.
# 2. Pickle module has no way to identify these threats or malicious data
# 1. dumps()->pickling
# There are four function in pickle module for pickling and un-pickling
# 2. loads()>un-pickling
# 3. dump()---->pickling----(store into file)
# 4. load()>un-pickling-->(read from file)

# ### `pickle` Module Interview Questions

# 1. What is the `pickle` module used for in Python?
#    - The `pickle` module is used for serializing and deserializing Python objects. Serialization is the process of converting a Python object into a byte stream, and deserialization is the reverse process.

# 2. How do you serialize an object using the `pickle` module?

import pickle
data = {'key': 'value', 'number': 42, 'list': [1, 2, 3]}
file = open('data.pkl', 'wb')
pickle.dump(data, file)
file.close()

# 3. How do you deserialize an object using the `pickle` module?

import pickle
with open('data.pkl', 'rb') as file:
    data = pickle.load(file)


# 4. What function is used to serialize an object to a string in the `pickle` module?

serialized_data = pickle.dumps(data)


# 5. What function is used to deserialize an object from a string in the `pickle` module?

deserialized_data = pickle.loads(serialized_data)


# 6. Can you `pickle` all Python objects?
#    - No, not all objects can be pickled. For example, file objects, database connections, and other objects with OS-specific or runtime-specific contexts cannot be pickled.

# 7. How do you handle pickling of custom objects?

#    class CustomObject:
#        def __init__(self, value):
#            self.value = value

#    obj = CustomObject(10)
#    with open('obj.pkl', 'wb') as file:
#        pickle.dump(obj, file)


# 8. How do you handle exceptions during the pickling process?

#    try:
#        with open('data.pkl', 'wb') as file:
#            pickle.dump(data, file)
#    except pickle.PicklingError as e:
#        print(f"Pickling error: {e}")


# 9. How do you handle exceptions during the unpickling process?

#    try:
#        with open('data.pkl', 'rb') as file:
#            data = pickle.load(file)
#    except pickle.UnpicklingError as e:
#        print(f"Unpickling error: {e}")


# 10. What are the security risks of using `pickle`?
#     - Unpickling data from an untrusted source can execute arbitrary code, which can lead to security vulnerabilities.

# 11. How can you mitigate security risks when using `pickle`?
#     - Only unpickle data from trusted sources, and consider using safer serialization formats like JSON for data exchange.

# 12. What is the difference between `pickle` and `cPickle`?
#     - `cPickle` is a faster implementation of `pickle` written in C. In Python 3, `cPickle` has been integrated into `pickle`, so using `pickle` automatically uses the optimized version.

# 13. How do you use `pickle` with Python's `with` statement?
 
#     with open('data.pkl', 'wb') as file:
#         pickle.dump(data, file)
#     with open('data.pkl', 'rb') as file:
#         data = pickle.load(file)
 

# 14. What is the `protocol` parameter in `pickle.dump()` and `pickle.dumps()`?
#     - The `protocol` parameter specifies the pickle protocol version to use. Higher protocols offer more efficient serialization but may not be compatible with older Python versions.

# 15. How do you specify a custom protocol version when pickling?
 
#     pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
 

# 16. What are the available pickle protocols?
#     - Protocol 0: Original ASCII protocol (backward compatible).
#     - Protocol 1: Old binary format (backward compatible).
#     - Protocol 2: Introduced in Python 2.3.
#     - Protocol 3: Introduced in Python 3.0.
#     - Protocol 4: Introduced in Python 3.4.
#     - Protocol 5: Introduced in Python 3.8.

# 17. How do you pickle multiple objects to the same file?
 
#     with open('data.pkl', 'wb') as file:
#         pickle.dump(data1, file)
#         pickle.dump(data2, file)
 

# 18. How do you unpickle multiple objects from the same file?
 
#     with open('data.pkl', 'rb') as file:
#         data1 = pickle.load(file)
#         data2 = pickle.load(file)
 

# 19. What is the purpose of `pickle.HIGHEST_PROTOCOL`?
#     - It specifies the highest available protocol version, providing the most efficient serialization.

# 20. How do you check if an object is picklable?
 
#     import pickle
#     try:
#         pickle.dumps(object)
#         print("Object is picklable")
#     except pickle.PicklingError:
#         print("Object is not picklable")
 

# ### `collections` Module Interview Questions

# 1. What is the `collections` module used for in Python?
#    - The `collections` module provides specialized container datatypes like `namedtuple`, `deque`, `Counter`, `OrderedDict`, and `defaultdict`.

# 2. What is a `namedtuple` and how do you create one?

#    from collections import namedtuple
#    Point = namedtuple('Point', 'x y')
#    p = Point(10, 20)


# 3. How do you access elements in a `namedtuple`?

#    print(p.x)  # Output: 10
#    print(p[0]) # Output: 10


# 4. What is a `deque` and how is it different from a list?
#    - A `deque` (double-ended queue) is optimized for fast appends and pops from both ends, unlike lists which are optimized for fast access.

# 5. How do you create and use a `deque`?

#    from collections import deque
#    d = deque([1, 2, 3])
#    d.append(4)
#    d.appendleft(0)


# 6. What is a `Counter` and how do you use it?
#    - A `Counter` is a dictionary subclass for counting hashable objects.

#    from collections import Counter
#    count = Counter(['a', 'b', 'c', 'a', 'b', 'b'])


# 7. How do you access elements in a `Counter`?

#    print(count['a'])  # Output: 2


# 8. How do you get the most common elements in a `Counter`?

#    most_common = count.most_common(2)


# 9. What is an `OrderedDict` and how does it differ from a regular `dict`?
#    - An `OrderedDict` remembers the order of insertion of items.

#    from collections import OrderedDict
#    od = OrderedDict()


# 10. How do you add items to an `OrderedDict`?
 
#     od['a'] = 1
#     od['b'] = 2
 

# 11. What is a `defaultdict` and how do you use it?
#     - A `defaultdict` is a dictionary that provides a default value for non-existent keys.
 
#     from collections import defaultdict
#     dd = defaultdict(int)
#     dd['a'] += 1
 

# 12. How do you specify a default factory for a `defaultdict`?
 
#     dd = defaultdict(lambda: 'default value')
 

# 13. How do you convert a regular dictionary to a `defaultdict`?
 
#     regular_dict = {'a': 1, 'b': 2}
#     dd = defaultdict(int, regular_dict)
 

# 14. How do you iterate over items in an `OrderedDict`?
 
#     for key, value in od.items():
#         print(key, value)
 

# 15. How do you merge two `Counter` objects?
 
#     count1 = Counter(['a', 'b', 'c'])
#     count2 = Counter(['b', 'c', 'd'])
#     merged_count = count1 + count2
 

# 16. How do you subtract counts using `Counter`?
 
#     subtracted_count = count1 - count2
 

# 17. How do you use `deque` as a stack and a queue?
 
#     stack = deque()
#     stack.append('element')  # Use as stack (LIFO)
#     queue = deque()
#     queue.append('element')  # Use as queue (FIFO)
 

# 18. How do you rotate elements in a `deque`?
 
#     d.rotate(1)
 

# 19. What are the advantages of using `deque` over lists for certain operations?
#     - `deque` is faster for appending and popping from both ends compared to lists.

# 20. How do you initialize a `Counter` with a dictionary?

