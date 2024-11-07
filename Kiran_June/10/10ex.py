# #if else statement
# #Syntax:--
# # if condition
# #     body_if
# # else:
# #     body_else
# """
# per=eval(input("Enter your percentage: "))
# if per>90:
#     print("You got government college congratulation!!!")
# else:
#     print("You have to take private college no option there sorry!")
 
# #1)Wap  to check a number is positive or negative
# num = eval(input("Enter a numbe: "))
# if num>0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# #2)Wap to check number is even or odd
# num = eval(input("Enter num: "))
# if num%2==0:
#     print("Enter number is even")
# else:
#     print("it is odd")

# #3)WAp to print square of even number and cube of odd numbers from a given list
# l = [1, 2, 3, 4, 5]

# for i in l:
#     if i % 2 == 0:
#         print(i**2)
#     else:
#         print(i**3)


# #4)Wap to print list of square of even numbers and  list of cube of odd numbers from a given list
l=[1,2,3,4,5] 
e=[]
o=[]
for i in l:
    if i%2==0:
        sq=i**2
        e.append(sq)
    else:
       cube=i**3
       o.append(cube)
print(e)
print(o)

# #OR
l=[1,2,3,4,5] 
e = []
o = []

for i in l:
    if i % 2 == 0:
        e.append(i**2)
    else:
        o.append(i**3)
print(e)
print(o)



# #Wap to print list of =>pass and print list of=> fail from a goven dict
Result={"Sanket":50,"svati":40,"ram":30,"Sham":20,"Aman":10}
pass_=[]
fail=[]
for name in Result:
    if Result[name] > 30:
        pass_.append(name)
    else:
        fail.append(name)
print(pass_)
print(fail)

#Wap to print dict of square of even and cube of odd number from 1 to 10
d=[]
for i in range(1,10):
    if i%2==0:
        d.append(i**2)
    else:
        d.append(i**3)   
print(d) 

d={}
for num in range(1,11):
    if num%2==0:
        sq=num**2
        d=[num]=sq
    else:
        cu=num**3
        d[num]=cu
print(d)


# #Adding Element
# d[key]=value

# #Accessing
# d[key]
# #OR
# d.get(key)

# #Updating Data
# d[key]=updated_value

# #Deleting
# Del d[key]

# #Removing
# d.pop(key)

# #Creating empty
# d={}
# # 













