### 1. Using map to Multiply Corresponding Elements of Two Lists
#    Question: Given two lists, list1 and list2, write a function that returns a new list containing the product of corresponding elements from list1 and list2 using map.
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
def mul(list1, list2):
    return list(map(lambda x,y:x*y,list1,list2))
print(mul(l1, l2)) 
"""

# ### 2. Filtering Even Numbers Using filter
#    Question: Write a function that takes a list of numbers and returns only the even numbers using the filter function.
"""
l1=[1,2,3,4,5,6]
def fil(l1):
    return list(filter(lambda x:x%2==0,l1))
print(fil(l1)) #[2, 4, 6]
"""

# ### 3. Using reduce to Compute the Product of a List
#    Question: Write a function that returns the product of all elements in a list using the reduce function.
"""
from functools import reduce
l1=[1,2,3,4,5]
def mul(l1):
    return reduce(lambda x,y:x*y,l1)
print(mul(l1))
"""
# ### 4. Combining map and filter
#    Question: Write a function that squares all even numbers in a list using map and filter.
"""
l=[1,2,3,4,5,6]
def comb(l):
    return list(map(lambda x:x**2,filter(lambda x:x%2==0,l)))
print(comb(l))
"""

# ### 5. Using map to Flatten a List of Lists
#    Question: Write a function that takes a list of lists and returns a flattened list using map.
"""
l = [[1, 2, 3], [4, 5], [6, 7]]
def flat():
    return [j for i in l for j in i]
print(flat()) #[1, 2, 3, 4, 5, 6, 7]
"""

# ### 6. Using reduce to Compute the Maximum Element
#    Question: Write a function that returns the maximum element from a list using reduce.
"""
from functools import reduce
l=[11,559,98,155,98,965]
def max(l):
    return reduce(lambda x,y:x if x>y else y,l)
print(max(l))
"""
# ### 7. Generating Fibonacci Sequence Using map
#    Question: Write a function that generates the first n Fibonacci numbers using map.
def fibo(n):
    l = [0, 1]
    list(map(lambda _: l.append(l[-1] + l[-2]), range(2, n)))
    return l[:n]
print(fibo(5))  # Output: [0, 1, 1, 2, 3]


# ### 8. Using filter to Extract Words Containing a Specific Letter
#    Question: Write a function that filters words from a list that contain a specific letter using filter.


# ### 9. Using map to Normalize a List of Values
#    Question: Write a function that normalizes a list of numbers to a range of 0 to 1 using map.

# ### 10. Using reduce to Compute the GCD of a List
#    Question: Write a function that computes the greatest common divisor (GCD) of a list of numbers using reduce.