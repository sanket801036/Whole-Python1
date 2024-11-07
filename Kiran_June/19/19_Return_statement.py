def f1():
    x=100
    return x#return must be write at end
x=f1()
print(x)#100

def f1():
    name="rajesh"
    age = 21
    city="pune"
    return name
f1()#you get nothig outpu

def f1():
    name="rajesh"
    age = 21
    city="pune"
    return name
print(f1())#rajesh

def f1():
    name="rajesh"
    age = 21
    city="pune"
    return name,age,city
print(f1())#('rajesh', 21, 'pune')

def f1():
    name="rajesh"
    age = 21
    city="pune"
    return name,age,city
name=f1()
print(name)#('rajesh', 21, 'pune')
print()

def f1():
    name="rajesh"
    age = 21
    city="pune"
    return name,age,city
name,age,city=f1()
print(name)#rajesh

def f1():
    x=100
    print("welcome")
    y=200
    z=300
    return x,y,z#(100, 200, 300)#ek se jyada return statement nhi likh skte
print(f1())#welcome
print("student") #student
print()
print()

#****nested Function
def f1():
    def f2():
        pass
x=100
def f1():
    y=200
    print(y)
    def f2():
        z=300
f1()#200

def f1():
    y=200
    print(y,x)
    def f2():
        z=300
f1()#200 100

print("Welcome to  main global scope ")
def f1():
    print("welcome to f1 function")
    y=200
    print(y,x)
    def f2():
        print("welcome to f2 function")
        z=300
        print(z)
f1()#300 not printed

def f1():
    print("welcome to f1 function")
    y=200
    print(y,x)
    def f2():
        print("welcome to f2 function")
        z=300
        print(z)
    f2()#300
f1()
print()

def f1():
    print("welcome to f1 function")
    x=10
    def f2():
        print("welcome to f2 function")
        y=30
    return f2
f2=f1()#welcome to f1 function
f1()#welcome to f1 function
print()

# def f1():
#     print("welcome to f1 function")
#     m=10
#     print(m)
#     def f2():
#         print("welcome to f2 function")
#         y=30
#     return m,f2 #now you got value of m which is 10
# f2=f1()#welcome to f1 function
# f1()

def f1():
    print("welcome to f1 function")
    x=10
    print(x)
    def f2():
        print("welcome to f2 function")
        y=30
    return x,f2
x=f1()#10
print(x)#10

#1:29

