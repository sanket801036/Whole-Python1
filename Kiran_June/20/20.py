"""
def f1():
    print("welcome to f1")
    def f2():
        print("welcome to f2")
        def f3():
            print("welcome to f3")
        return f3
    return f2
f2=f1()
f3=f2()   
f3()

def f1():
    print("welcome to f1")
    a=10
    def f2():
        print("welcome to f2")
        b=20
        def f3():
            print("welcome to f3")
            c=30
            def f4():
                print("welcome to f4")
                d=40
                def f5(): 
                    print("welcome to f5")
                    e=50
                    print(a,b,c,d,e)
                return f5#return e,f5               
            return f4#return d,f4          
        return f3#return c,f3
    return f2#return b,f2
f2=f1()#a,f2=f1
f3=f2()#b,f3=f2
f4=f3()#c,f4=f3
f5=f4()#d,f5=f4
f5()
       


#1) positiona parameter
def num(a,b,c):
    sum=a+b+c
    return sum
print("sum is:",num(1,2,3))#need to maintain position

#2)keyword argument
def num(a,b,c):
    sum=a+b+c
    return sum
print("sum is:",num(a=1,b=2,c=3))#no need to maintain position bu no. of parameter must be equal to no. od argument

#3)Default argument
def num(a,b,c=50):#default argument be at end ,if not then you must make avery parameter default
    sum=a+b+c
    return sum
print("sum is:",num(1,2))
print("sum is:",num(1115,214548))

def num(a=10,b,c):#SyntaxError: parameter without a default follows parameter with a default
    sum=a+b+c
    return sum
print("sum is : ", num(1,2))
"""
#4)Arbitary argument
def num(*x):
    print(x)
print(num(1,2,3))
#1)positional arbitary
def num(**x):
    print(num)
# print(num(1="sanket",2="ram"))
#2)keyword arbitary


#Logical Quest