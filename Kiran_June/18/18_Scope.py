#Functional Scope
x=100                           #Function Global scope
y=200                           #Functional GLobal Scope(x,y is Global scope variable)
def f1():
    a=10                        #Functional Local scope
    b=20                        #Functional Local scope(a,b is local scope variable)
    print(a,b)#you got nothing(usko call nhi kiya)
print(x,y) #100 200#safe attribute ke vajah se yaha pr space aa jati hai
print()


x=100                           #Function Global scope
y=200                           #Functional GLobal Scope(x,y is Global scope variable)
def f1():
    a=10                        
    b=20                        
    print(a,b)
print(x,y) #100 200
f1() #10 20
print()

x=100                           
y=200                          
def f1():
    a=10                        
    b=20                        
    print(x,y)
f1() #100 200
print("-------------------------------")


a=12
def inc():
    a=a+1#cannot access local variable 'a' where it is not associated with a value
    print(a)
inc()# (global variable ko acces kr skte hai pr change nhi kr skte)


a=12
def inc():
    global a#(global keyword ka use karenge to apan change kr skte hai)
    a=a+1
    print(a)
inc()#13
print()

x=100
def f1():
    a=10
    b=20

# f1()
# print(x)
# print(a,b)#name 'b' is not defined

x=100

def f1():
    a=10
    b=20
f1()
print(x)
print(a,b)# name 'b' is not defined

#Globel scope
#Local Scope
