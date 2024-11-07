# l.append(l1)   --=>old.append(new)
# l.extend(l1)   --=>old.extend(new) 
# print(l.index(55))
# print(l.count(11) --=>`count` does not search within nested lists.
# l.reverse()       --=>

### List Operations
# 1. Append:
l1 = [11, 22, 33]
l2 = [44, 55, 66]
l1.append(l2)
print(l1)
# Output: `[11, 22, 33, [44, 55, 66]]`

# 2. Extend:
l1 = [11, 22, 33]
l2 = [44, 55, 66]
l1.extend(l2)
print(l1)
# Output: `[11, 22, 33, 44, 55, 66]`
# Concept: `extend` adds elements of the list individually.

# 3. Count:
l = [11, 22, 33, 11, 11, 55]
print(l.count(11))
#  Output: `3`
   
# 4. Index:
l = [11, 22, 33, 55]
print(l.index(55))
# Output: `3`

# 5. Nested Count:

l = [11, 22, 33, [11, 22, 111], 11, 77]
print(l.count(11))

# Output: `2`
#    Concept: `count` does not search within nested lists.

# 6. Reverse:
l = [11, 22, 33, 55]
l.reverse()
print(l)
#    Output: `[55, 33, 22, 11]`
#    Concept: `reverse` reverses the list in place.

# 7. Sort:
l = [11, 22, 1, 8]
l.sort()
print(l)
#    Output: `[1, 8, 11, 22]`
#    Concept: `sort` sorts the list in place.

# 8. Sorted Function:
l = [11, 22, 1, 8]
print(sorted(l))
print(l)
#    Output: [1, 8, 11, 22]
#  #         [11, 22, 1, 8]  
#    Concept: `sorted` returns a new sorted list, original list remains unchanged.

### Set Operations
# 1. Set Initialization and Uniqueness:
s = {11, 22, 22, 33, 44, 55, 55, 55}
print(s)
#    Output: `{11, 22, 33, 44, 55}`
#    Concept: Sets automatically remove duplicates.

# 2. Mutable Set:
t = {11, 22, 33, 44, 55}
t.add(77)
print(t)

#    Output: `{33, 11, 44, 77, 22, 55}`
#    Concept: Sets are mutable; elements can be added.

# 3. Invalid Set Elements (List and Dict):

s = {11, 12.89, 3+7j, "Sanket", [55, "linda"]}
print(s) # TypeError: unhashable type: 'list'           ***********************************************************************************

s = {11, 12.89, 3+7j, "Sanket", {55, "linda"}}
print(s) # TypeError: unhashable type: 'set'            **********************************************************************************
#    Concept: Sets cannot contain mutable types like lists or other sets.

# 4. Empty Set:
s = {}
print(type(s)) # <class 'dict'>

s = set()
print(type(s)) # <class 'set'>

#    Concept: `{}` initializes an empty dictionary, `set()` initializes an empty set.

### String Operations
# 1. Replace:
l = "My Keeran Academy"
l2 = l.replace("ee", "i")
print(l)
print(l2)
#    Output: 
#    My Keeran Academy
#    My Kiran Academy
#    Concept: `replace` returns a new string, original string remains unchanged.

### List Element Update
# 1. Update List Elements:
l = [11, 22, 33, 44, 55]
l[2] = 333
print(l)

#    Output: `[11, 22, 333, 44, 55]`
#    Concept: Lists are mutable, elements can be updated by index.

# 2. Update Nested List Elements:
l = [11, 22, [33, 44], 55, 66]
l[2][1] = 333
print(l)
#    Output: `[11, 22, [33, 333], 55, 66]`
#    Concept: Elements within nested lists can also be updated.

