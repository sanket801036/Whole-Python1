# s=lambda a,b:a if a>b else b
# print(s(10,20))#20

#Recursion
#A function that calls itself is known as recursive function
# fact()=3*2*1
# fact()=2*1
# fact()=1
# fact()=1

# fact(3)=3*fact(2)
# fact(n)=n*fact(n-1)
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#     return result
# print(fact(4))#24

#What is  diff between print() and return statement in python function
def add(a,b):
    return(a+b)
def square(x):
    return(x*x)
result = add(10,20)
print(result)#30
print(square(result))#900
