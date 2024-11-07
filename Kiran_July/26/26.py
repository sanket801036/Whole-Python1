# #import module
# import math
# print(math.factorial(5))#120
# print(math.cos(0.4645648))#0.8940166345592775  

# #from module import fun1,fun2,fun3...
# from math import factorial,sin 
# print(math.factorial(5))   #120
# print(math.)

# from math 
# factorial(5))

#Decorator***************************
# def deco(fun):
#     def inner():
#         fun()
#         print("hello")
#         print("hello")
#     return inner

# def printer():
#     print("hello")
#     print("hello")
#     print("hello")
# printer = deco(printer)
# printer()


# def deco(fun):
#     def inner():
#         fun()
#         print("hello")
#         print("hello")
#     return inner
# @deco
# def printer():
#     print("hello")
#     print("hello")
#     print("hello")
# printer = deco(printer)
# printer()
# # hello
# hello
# hello
# hello
# hello
# hello
# hello

# def deco(fun):
#     def inner():
#         result=fun()
#         n3=eval(input("Enter 3nd: "))
#         return result+n3
#     return inner
# @deco
# def sum():
#     n1=eval(input("Enter 1s: "))
#     n2=eval(input("Enter 2nd: "))
#     result=n1+n2
#     return result
# sum()

# def deco(fun):
#     def capital():
#         result=fun()

# @deco
# def f_name():
#     n1=input("Enter your first name: ")
#     n2=input("Enter your last name: ")
#     return n1+" " +n2
    
# print(f_name())

"""
def deco(fun):
    def inner(n1,n2,n3):
        result=fun(n1,n2)
        return result*n3
    return inner

@deco
def mul(n1,n2):
    return n1*n2
print(mul(12,2,3))
"""


def to_uppercase(fun):
    def capital(n1, n2):
        result = fun(n1, n2)
        return result.upper()
    return capital

@to_uppercase
def f_name(n1,n2):
    return n1+" " +n2    
print(f_name("sanket","kolhe"))

