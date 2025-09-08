# # Sure! Here are 22 practical interview questions and answers on Python lists, followed by 20 questions and answers on list methods. 

# # ### Practical Interview Questions on Python Lists

# # 1. What is a list in Python?
# #    - OMH collection of element

# # 2. How do you create a list in Python?

# l = [1, 2, 3, 4, 5]

# # 3. How do you access elements in a list?
# #    - You can access list elements by their index.
# l = [1, 2, 3, 4, 5]
# f=l[0]
# print(f)#1

# # 4. How do you modify an element in a list?
# l = [1, 2, 3, 4, 5]
# l[0] = 10
# print(l)#[10, 2, 3, 4, 5]

# # 5. How do you add an element to a list?
# l = [1, 2, 3, 4, 5]
# l.append(6)
# print(l)#[1, 2, 3, 4, 5, 6]


# # 6. How do you remove an element from a list by value?
# l = [1, 2, 3, 4, 5]
# l.remove(3)
# print(l)#[1, 2, 4, 5]

# # 7. How do you remove an element from a list by index?
# l = [1, 2, 3, 4, 5]
# del l[1]
# print(l)#[1, 3, 4, 5]

# # 8. How do you find the length of a list?
# l = [1, 2, 3, 4, 5]
# le = len(l)
# print(l)#[1, 2, 3, 4, 5]

# # 9. How do you check if an item is in a list?
# l = [1, 2, 3, 4, 5]
# e = 3 in l
# print(e)#True

# # 10. How do you iterate through a list?
# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i)
# # 1
# # 2
# # 3
# # 4
# # 5


# # 11. How do you slice a list?
# l = [1, 2, 3, 4, 5]
# s = l[1:3]
# print(s)#[2, 3]

# # 12. How do you concatenate two lists?
l = [1, 2, 3, 4, 5]
n=l+[7, 8, 9]
print(n)#[1, 2, 3, 4, 5, 7, 8, 9]

# # 13. How do you copy a list?
l = [1, 2, 3, 4, 5]
c=l[:]
print(c)#[1, 2, 3, 4, 5]

import copy
original_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)
print(deep_copy)  # [[1, 2], [3, 4]]

shallow_copy = original_list.copy()

# # 14. How do you find the index of an element in a list?
l = [1, 2, 3, 4, 5]
i = l.index(3)
print(i)#2

# # 15. How do you sort a list?
l = [3, 1, 4, 1, 5, 9, 2, 6, 5]
l.sort()
print(l)#[1, 1, 2, 3, 4, 5, 5, 6, 9]

# # 16. How do you reverse a list?
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)#[5, 4, 3, 2, 1]

# # 17. How do you insert an element at a specific index in a list?
l = [1, 2, 3, 4, 5]
l.insert(2, 20)
print(l)#[1, 2, 20, 3, 4, 5]

# # 18. How do you remove and return an element from a list?
l = [1, 2, 3, 4, 5]
i= l.pop(2)
print(i)#3

# # 19. How do you count the occurrences of an element in a list?
# l = [1, 2, 3, 4, 5]
# c= l.count(2)
# print(c)#1

l = [1, 2, 3, 4, 5, 2, 2]
element_to_count = 2
counter = 0

for item in l:
  if item == element_to_count:
    counter += 1

print(f"The element {element_to_count} appears {counter} times.")



# # 20. How do you clear all elements from a list?
# l = [1, 2, 3, 4, 5]
# l.clear()
# print(l)#[]

# # 21. How do you create a list with repeated elements?
# l = [1, 2, 3, 4, 5]
# l = [0]*5  
# print(l)#[0, 0, 0, 0, 0]

# # 22. How do you create a list using a list comprehension?

# squares = [x**2 for x in range(10)]
# print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Sure! Here are the practical interview questions on Python lists based on the examples provided:

### Practical Interview Questions on Python Lists

# 13. How do you copy a list?
l=[1,2,3,4,5,6]
m=l.copy()
print(m)   #[1, 2, 3, 4, 5, 6]

# 16. How do you reverse a list?
l=[1,2,3,4,5,6]
r=l[::-1]
print(r)#[6, 5, 4, 3, 2, 1]

l=[1, 2, 3, 4, 5]
l.reverse()
print(l)  # Output: [5, 4, 3, 2, 1]

#This returns an iterator that accesses the given sequence in the reverse order.
l= [1, 2, 3, 4, 5]
r = list(reversed(l))
print(r)  # Output: [5, 4, 3, 2, 1]


l=[1, 2, 3, 4, 5]
r=[]
for i in l[::-1]:
    r.append(i)
print(r)  # Output: [5, 4, 3, 2, 1]

l = [1, 2, 3, 4, 5]
r = [l[i] for i in range(len(l)-1, -1, -1)]
print(r)  # Output: [5, 4, 3, 2, 1]


# 18. How do you remove and return an element from a list?
l = [1, 2, 3, 4, 5]
i= l.pop(2)
print(i)#3

l = [1, 2, 3, 4, 5]
l *=2  
print(l)#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]   **************************************************

# 21. How do you create a list with repeated elements?
l = [1, 2, 3, 4, 5]
l = [5]*5  
print(l)#[5, 5, 5, 5, 5]

