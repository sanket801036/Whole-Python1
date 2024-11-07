#practicle
# print("hello")
# print(10/0)
# print('divya')


# print("hello")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("zero in denominator is not allow ")
#     print(10/2)
# print('divya')

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print('Exception Error: ',msg)#Exception Error:  division by zero
# #try with multiple except block
# print("=======")


# try:
#     x=int(input('enter 1st number'))
#     y=int(input('enter 2nd number'))
#     print(x/y)
# except ZeroDivisionError:
#     print('can t divided by zero')
# except ValueError:
#     print('please provide int value')
# print("==========================================")
# try:
#     x=int(input('enter 1st number'))
#     y=int(input('enter 2nd number'))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#     print('please check : ',msg)   

# try:
#     x=int(input('enter 1st number'))
#     y=int(input('enter 2nd number'))
#     print(x/y)
# except ZeroDivisionError:
#     print("zero division error")
# except:
#     print("default except: please provide valid input")

# try:
#     fp=open("test2.txt",'r')
#     data=fp.read()
#     print(data)
# except FileNotFoundError:
#     print("file not found error")
# finally:
#     fp.close()
# data1=fp.read()
# print(data1)

try:
    print("try")
except:
    print("except")
finally:
    print("finally")

try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except zero division error")
finally:
    print(

        
    )