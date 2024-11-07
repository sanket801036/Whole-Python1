# #Higher order function
# #Write a python program to filter the list by even numbers
# # l=[11,22,33,44,55]
# # m=[]
# # for i in l:
# #     if i%2==0:
# #         m.append(i)
# # print(m)

# # def even():
# # l=[11,22,33,44,55]
# # def even(seq):
# #     l=[]
# #     for num in seq:
# #         if num%2==0:
# #             l.append(num)
# #     return l
# # print(even(l))

# # l=[11,22,33,44]
# # def even(seq):
# #     if

# # l=[11,22,33,44,55]
# # nl=list(filter(lambda num : num%2==0,l))
# # print(nl)

# l=[11,22,33,44,55]
# def odd(seq):
#     nl=[]
#     for num in seq:
#         if num%2!=0:
#             nl.append(num)
#     return nl
# print(odd(l))
# l=[11,22,33,44,55]
# nl=list(filter(lambda num : num%2!=0,l))
# print(nl)

#Write a proogram to print the elements of the list which is started from r
# name=['raj','rajesh','pavan','kunalm','sanket','ram']
# st=list(filter(lambda n: n.startswith('r'), name))
# print(st)
# #Orsr=list(filter(lambda n: ('
# st1=list(filter(lambda n: n.endswith('m'), name))
# print(st1)

# name=['raj','RAJESH','pavan','kunalm','SANKET','ram']
# #up=(filter(lambda name:name=name.upper(name),name))
# nl=list(filter(lambda name:name.isupper(),name))
# print(nl)
# name=["Nagpur","Pune","shegaon","khamgaon","amravati"]
# st1=list(filter(lambda n: n.endswith('gaon'), name))
# print(st1)
# name=["Nagpur","Pune","shegaon","khamgaon","amravati"]
# st2=list(filter(lambda names:name[-4:]=="gaon", name))
# print(st2)
#write a python program to print divisible by 3 and 4
# l = [11, 22, 4, 12, 3, 55]
# d = list(filter(lambda num: num % 3 == 0 and num % 4 == 0, l))
# print(d)

# Set Programs

# Find the size of a Set in Python
# s={11,22,33,44,55,66,77,88,99}
# print(len(s))


# Iterating over the set
# m= {1, 2, 3, 4, 5}
# for i in m:
#     print(i)

# Python-Maximum and Minimum in a Set
# print(min(m))
# print()
# print(max(m))
# Python - Remove items from Set
# m.remove(3)
# m.discard(1)
# print(m)
# Python - Check if two lists have at least one element common
# a={151,5465,686,8798,6565,6515,321}
# b={1651,5151,32151,321,6565,6515,321}
# print(a&b)
# Python program to find common elements in three lists using sets 
# a={151,5465,686,8798,6565,6515,321}
# b={1651,5151,32151,321,6565,6515,321}
# c={321,546,8,64,94,69}
# print(a&b&c)

# Python - Find missing and additional values in two lists
a={151,5465,686,8798,6565,6515,321}
b={1651,5151,32151,321,6565,6515,321}
print(a - b)
# Python program to find the difference between two lists
print(a - b)
# Python Set difference to find lost element from a duplicated array

# Python program to count number of vowels using sets in given string


# Concatenate the uncommon characters

# Python - Program to accept the strings which contains all vowels