"""
# 1)Write a Python Progrem to find out common letters between two strings
def common():
    a=input("first string: ")
    b=input("second string: ")
    s1=set(a)
    s2=set(b)
    c = s1 & s2
    print(c)
common()
"""
#Wap to count the frequency of words appearing in a string
# def count():
#     s=input("Enter string: ")
#     d={}
#     for i in s.split():
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     print(d)
# count()
# def freq():
#     s=input("Enter string: ")
#     l=s.split()
#     d={}
#     for i in l:
#         d[i]=d.get(i,0)+1
#     print(d)

# freq()
def find_anagrams(string_list, target):
    sorted_target = sorted(target)
    anagrams = list(filter(lambda x: sorted(x) == sorted_target, string_list))
    for anagram in anagrams:
        print(anagram)
