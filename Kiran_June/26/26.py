#write a program to find even or odd using function
# def check():
#     num = int(input("Enter a number:"))
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# check()

#Write peogram to check given number is prime or not

# def check():
#     num = eval(input("Enter a number:"))
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not prime")
#         else:
#             print("Prime")
#             break
# check()

#Write peogram to check given number is prime or not.usint only if else not for loop
# def check():
#     if num % i == 0:
#         print("Not prime")
#     elif num %
#
#Write program to find palindrom 
# def is_pal(word):
#     if s(word) == s(word)[::-1]:
#         return 'palindrome'
#     else:
#         return 'not palindrome'
# print(is_pal("madam"))

#Write a function to find palindrom by using for loop

# def is_pal(word):
#     for i in range(len(word) // 2):
#         if word[i] != word[len(word) - i - 1]:
#             return "not palindrome"
#     return "palindrome"

# print(is_pal("madam"))

#write a function to print given string in reverse order like string the will converted to eht
#s="The kiran academy is good institue"

# def reve(s):
#     s = s[::-1]
#     return s

# print(reve(s))#eutitsni doog si ymedaca narik ehT

#*******IMPORTANT*******
# l=s.split()
# print(l)
# p=[]
# for i in l:
#     p.append(i[-1]+i[1:len(i)-1]+i[0])
# print(p)
# s1=' '.join(p)
# print(s1)

# s="the sky is blue"
# #o/p='blue is sky the'
# l=s.split()
# print(l)#['the', 'sky', 'is', 'blue']
# p=[]
# for i in l:
#     p.append(i[3]+i[2]+i[1])

# s1=' '.join(p)
# print(s1)

# # def reverse(string):
# #     string = "".join(reversed(string))
# #     return string
# #     print("The reversed string is : ", end="")
# #     print(s)

# # print(reverse(s))
l=[1,44,55,67,58]
m = l[0]
for num in l:
    if num > m:
        m = num
print(m)

#max
#sort list without using sort keyword
#s=[10,35,8,96,44]#in ascending order
l = [10, 35, 8, 96, 44]
n = len(l)
for i in range(n):
    for j in range(0, n-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)
s=[7,8,9,5,2]
                # find pair of numbers from the list whose addtion is 10
