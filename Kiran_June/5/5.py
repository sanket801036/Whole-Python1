#Rivision
# values()==>[v1,v2....]
# keys() ==>[(k,v),(k,v)...]
# items() ==>[(k,v),(k,v)...]
# List ke case mein pop(value) leta hai


#range()
#Syntax:range(start_value,end_)
# start_value:start_valueend_value :before end vakue
# step_value
"""
r=range(1,6,1)
print(r)
print(type(r))

r=range(1,6,1)
for num in r:
    print(num)

#Q1 Wap to print numbers from 11-20
r=range(1,21,1)
for num in r:
    print(num)

#Q2.Wap to print even numbers from 21-31
r=range(22,31,2)
for num in r:
    print(num)

#Q3.Wap to print even numbers from 21-31
r=range(21,32,2)
for num in r:
    print(num)

r=range(50,29,-2)
for num in r:
    print(num)

#Q4 Wap to print list of numbers from 1 to 50
l=[]
for num in range(1,51,1):
    l.append(num)
print(l)

l=[47,45]
for num in range(47,38,-2):
    l.append(num)
print(l)

#Wap to print set of square of umbers from 10-20
s=set()
for num in range(10,21,1):
    s.add(num*num)**********************************************************
print(s)

#Wap to print set of cube  of num umbers from 3-9
s=set()
for num in range(3,10,1):
    s.add(num*num*num)
print(s)

#Wap to print set of cube  of num umbers from 3-10
s=set()
for num in range(6,12,2):
    s.add(num*num*num)
print(s)

employee={"Sanket":200000,"Ravi":15000,"Sam":2000}
#print(employee["Ravi"])
# employee["sanket"]=employee["sanket"]+2000
# print(employee)
for name in employee:
    employee[name]=employee[name]+2000
print(employee)

employee={}
for i in range(2):
    name=input("enter name:")
    salary=eval(input("enter salary"))
    employee[name]=salary
print(employee)
"""
for i in range(1,6,1):
    print(i)

for i in range(1,6):
    print(i)

for i in range(6):
    print(i)

for i in range(10):
    print("Sanket")







