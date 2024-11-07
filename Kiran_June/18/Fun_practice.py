#Create a function to print a cube of number 
def fun():
    x=int(input("Enter the number: "))
    print(f"The cube of{x}is{x**3}")
fun()

# #create a function to print table of any number
def table():
    num=int(input("Enter the number"))
    for i in range(1,11):
        print(num*i)
table()

# #Wap list of vowel from given string
def vowels():
    l = []
    s = input("Enter string :")
    for i in s:
        if i in "aeiou":
            l.append(i)
    print(l)
vowels()

#Wap to print list of number from given string
def a():
    l=[]
    a=input("enter string: ")
    for i in a:
        if i.isdigit():                 # **********************************
            l.append(i)
    print(l)
a()

#Wap to print list of length of each string from given list
def num():
    l=[]
    num=input("enter :")
    for i in l:
        if i.isdigit():
            l.append(i)
num()

#Wap to print list of length of each string fwom given list
l=["priti","jay","sidhant"]
l1=[]
def a():
    for i in l:
        l1.append(len(i))
    print(l1)
a()#[5, 3, 7]

# l=["priti","jay","sindhant"]
# def s():
#     for i in range(len(l)):
#         l[i] = l[i].capitalize()
#     print()
# s()
#Task
# string = "Welcome to JBK":
# calculate length of string without using length() function - for Loop
# 1)To display  1-10 numbers :-even numbers by using for Loop
for i in range(1,11):
    if i%2 == 0:
        print(i)
# Output:-
#          2
#          4
#          6
#          8
#          10


# 2) To display 10 -1 numbers :- odd numbers using for loop 
for i in range(11,1):
    if i%2!=0:
        print(i)

# 3)to display sum of 1 to 10 numbers
sum=0
for i in range(1,11):
    sum = sum + 1
print(sum)#10

# 4) to display number uin reverse order
num = 123
sum = 0
while num !=0:
    r = num%10
    sum=sum*10+r
    num = num//10
print(sum)#321
    


