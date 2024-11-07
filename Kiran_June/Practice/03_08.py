# import random

# # Generate 20 random numbers between 1 and 485
# random_numbers = random.sample(range(1, 486), 20)

# print(random_numbers)
# [176, 71, 326, 59, 203, 285, 175, 205, 130, 461, 50, 124, 322, 179, 95, 147, 300, 435, 438, 464]

# 176) How can you use a loop to sum the elements of a list?
l=[1, 2, 3, 4, 5]
s=0
for i in l:
   s = s + i 
print(s) #15

#71) How do you sort a dictionary by keys or values?
d = {"sanket": 10, "swity": 20, "mummy": 50, "papa": 10}
s = {}
sort = sorted(d.keys())
for key in sort:
    s[key] = d[key]
print(s)#{'mummy': 50, 'papa': 10, 'sanket': 10, 'swity': 20}

# 326)What is the `functools.partial` function and how is it used?
# functools.partial` is used to fix a certain number of arguments of a function and generate a new function.
from functools import partial
def power(base, exponent):
        return base ** exponent
square = partial(power, exponent=2)
print(square(4))  # Output: 16

#59)How do you perform dictionary addition?
d1={"a":1,"b":2}
d2={"c":3,"d":4}
c = d1.copy()
c.update(d2)
print(c)        #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Using Dictionary Unpacking
d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4}
c={**d1,**d2}
print(c)        #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dictionaries to combine
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# Using a Loop
c={}
for i,j in d1.items():
    c[i]=j
for i, j in d2.items():
    c[i]=j
print(c)        #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 203)How can `return` be used to exit from nested functions?
def outer():
    def inner():
        return "Returned from inner"
    return inner()
print(outer()) #Returned from inner

# 285) Write a function that returns the factorial of a number using a nested function.
def fact(n):
    def inner(n):
        if n == 0:
            return 1
        else:
            return n * inner(n-1)
    return inner(n)  
print(fact(5)) #120

# 175)