s = "Create a set from  a string to get unique"
n=set(s)
print(n)

#Problem 2: Intersection of Set
#Problem Statement:
# Given two sets, return their intersection
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1.intersection(set2)
print(set3)

#Problem 3: Difference of Sets 
#Problem Statement:
#Given two sets,return the difference(element in the first set but not in the second set)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1.difference(set2)
print(set3)  # Output: {1, 2}

#Problem 1:Unions of sets
#Problem Statement:
#Given two sets ,return their union
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5, 6, 7}

#Problem5 :Check Subset
#roblem Statement:
#Chaeck if the first set is a subset of the second set

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1.issubset(s2)
print(s3)  # Output: False

#Problem 6: Check Superset
#Problem Statements:
#Check if the first set is a superset of second set

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1.issuperset(s2)
print(s3)  # Output: False

#Problem 7: Convert List to set
#Problem Statement:
#Convert a list to set to remove duplicates
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = set(l)
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Convert a set to list to remove duplicates

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
l = list(s)
print(l)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Problem 8: Set Length
# Problem Statement
# Find the number of unique elements in a set   

s = {1, 2, 3, 4, 5, 6, 7, 3, 2, 5}
print(len(s))  # Output: 

#problem 9: Add Element to Set
#Problem Statement:
#Add a new element to the set

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 6}

#Problem 10:Update a Set with Another Set
#Problem Statement
#Update a Set with the intersection of itself and another set

s1 = {1, 2, 3, 4, 5}

s2 = {3, 4, 5, 6, 7}

s1.intersection_update(s2)

print(s1)  
print(s2)
print("-------------------")

#Problem 11: Update a Set with Difference
#Problem Statement:
#Update a Set with Difference to itself and another set
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s1.difference_update(s2)
print(s1) # {1, 2}

#Problem 12: Remove Element From Set
# Problem Statement:
# Remove an element from a set if it it exists.
s = {1, 2, 3, 4, 5}
s.discard(4)
print(s)  

#Problem 13: Check Disjoint Sets 
# Problem Statement:
# Check it two sets are disjoint(have no elements in common).
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}
s3 = s1.isdisjoint(s2)
print(s3)  

#Problem 12:Clear a Set
#Problem Statement:
#Remove all elements from the set
s = {1, 2, 3, 4, 5}
s.clear()
print(s)  # Output: set()

#Problem 13:Copy a Set
#Problem Statement:
#Create a shallow copy of the set
s1 = {1, 2, 3, 4, 5}
s2 = s1.copy()
print(s2) 

#Problem 14:Pop an Element from a Set
#Problem Statement:
#Remove and return an arbitrary element from the set
s = {1, 2, 3, 4, 5}
s.pop()
print(s)  # Output: {2, 3, 4, 5}

#Problem 15:Update a set with Another Set 
# Problem Statement
# Update a set with union of itself and another set

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s1.update(s2)
print(s1) 

#Tuple
t = (11,"raj","kunal",33)
print(t[1:3])

t = (11,22,33,44,[66,77,88])
print(t[-3::-1])



my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
list_size = len(my_list)
tuple_size = len(my_tuple)

print("Size of the list:", list_size)
print("Size of the tuple:", tuple_size)

if list_size > tuple_size:
    print("The list is larger than the tuple.")
elif list_size < tuple_size:
    print("The tuple is larger than the list.")
else:
    print("The list and the tuple have the same size.")


# List	      Tuple
# 1.[]	      1.()
# 2.Mutable	  2.immutable
# 3.[]	      3.
# 4.Size is more   	   4.Sixe is less
# 5.Speed is less  	   5.Speed is more
# 6.data is chnageble   	Data is fix used tuple
	































