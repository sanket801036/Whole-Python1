nl=[num for num in range(1,11)]
print(nl)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s=[num for num in num**2]
# print(s)
l=[1,2,3,4,5]
l1=[]
for i in l:
    i=i**2
    l1.append(i**2)
print(l1)#[1, 16, 81, 256, 625]

l2=[num**2 for num in l]
print(l2)

l=[10,20,30,40]
k=[n/2 for n in l]
print(k)#[5.0, 10.0, 15.0, 20.0]

l=[1,2,3,4,5,6]
odd=[]
for num in l:
    if num %2!=0:
        odd.append(num)
print(odd)

l=[1,2,3,4,5,6]
odd=[num for num in l if num %2!=0]
print(odd)

l2=[1,2,3,4,5,6]
even=[num for num in l2 if num %2==0]


l=[1,2,3,4,5,6,7]
s=[num**2 for num in l if num %2!=0 ]
print(s)

l = ["ajay", "vijay", "rajendra", "pavankumar"]
k = [len(name) for name in l]
print(k) # [4, 5, 8, 10]

l = ["ajay", "Vijay", "rajendra", "Pavankumar"]
u = [i for i in l if i[0].isupper()]
print(u) # ['Vijay', 'Pavankumar']

# l=[1,2,3,4,5]
# d={}
# for i in l:
    # d.append()
#nd={k:v for var in seq}
l=[1,2,3,4,5]
square={num:num**2 for num in l}

c={num:num**3 for num in range(5,10)}
print(c)
print()
#nd={k:v for var in seq if cond}
# nd={num:num**2 for num in l if num%2==0}

nc={num:num**3 for num in range(11,20) if num%2!=0}
print(nc)

