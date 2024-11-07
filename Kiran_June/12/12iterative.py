# #Iterative
# #>for loop
# #>while loop transfer statement#jab tak condtion false nhi hoti tabtak  while loop chalenga
# #Syntax
# # ICU
# while CONDTION:
#     body
#     #statement
#     UPDATE
# #EX:-
# i=1
# while i<10:
#     print(i)
#     i=i+1
# print("Hello")

# #WAP  to print square of numbers from 1 to 10 by using while
# i=1
# while i<=10:
#     print(i*i)
#     i=i+1

# #WAP to print dict of cube of numbers from 11-20 by using while loop
# i=11
# l=[]
# while i<=20:
#     cu=i**3
#     l.append(cu)
#     i=i+1
# print(l)
# #OR
# i=11
# l=[]
# while i<=20:
#     l.append(i**3)
#     i=i+1
# print(l)

# #WAP to print dict of square of numbers from 1-5 by using while loop
# i=1
# d={}
# while i<=5:
#     sq=i**i
#     d[i]=sq
#     i=i+1
# print(d)

# #l=[1,2,3,4,5,6]
# #WAP to print square of numbers=>list by using while loop
# l=[1,2,3,4,5,6]
# i=0
# while i<len(l):
#     print(l[i]**2)
#     i+=1

# l=["raj","sanket","sham"]
# for i in l:
#     print(i)

# #transfer statement:
# # pass
# # continue
# # break
# #
# #if condition:#IndentationError: expected an indented block after 'if' statement on line 66# sometime code we vand to left then we use "pass"
# #continue#currentiteration ko skip krta hai

# l=[11,22,33]
# for i in l:
#     continue
# print(i)

# #break
# l=[11,22,33,44,55,66]
# for i in l:
#     if l==22:
#         break
#     print(i)


# #Calculate the discount based on the total purchase amount 
# #Problem statement:Calculate the final amount after applying a discount based on the total purchase amount.The discounts are:20% for purchases of 500 or more,10% for purchases between 200 and 499, and no discount for purchases below 200.
# amount=eval(input("enter amount "))
# if amount>=500:
#     print(a*20/100)
# elif amount >=200 :
#     print(amount*10/100)
# else:
#     print("Invalid")

# #Determine the season based on month number.
# #Problem statement:Determine the season based on the month number (1-12).The seasons are :Winter for december,january,and february;Spring for march,April and May;Summer for June,July, and August; and Autumn for September,Octomber,and November.
# month-eval(input("enter month number:  "))
# if month in  [12,1,2]:
#     print("winter")
# elif month in [3,4,5]:
#     print("spring")
# elif month in [6,7,8]:
#     print("summer")
# elif month in [9,11]:
#     print("Autumn")    

# # Calculate the final selling price after applying a series of discount.
# #Problem statement:Calculate the final selling price after applying a series of successive discount.The first discount is 10% off the original price, and the second discount is 5% off the price after the fisrt discount
