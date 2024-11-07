# append  --=>l.append(99)   # direct element
# insert  --=>l.insert(1,99) # index and value   
# remove  --=>l.remove(99)   # direct element
# pop     --=>l.pop(99)      # direct element
# del     --=>del l[1]       # del var[index]
# clear   --=>l.clear()      # it should be empty
# copy    --=>l1 = l.copy()  # new list equal to old and empty

l = ["Sanket","Tularam","Kolhe"]
l.append("JBK")#['Sanket', 'Tularam', 'Kolhe', 'JBK']
print(l)

numbers = [11,22,33,[44,55,66],77,88]
numbers.append(999)#[11, 22, 33, [44, 55, 66], 77, 88, 999]
print(numbers)

numbers[3].append(888)#[11, 22, 33, [44, 55, 66, 888], 77, 88, 999]
print(numbers)

numbers = [11,22,33,[44,55,66,["raj","pavan"]],77,88]
numbers[3][3].append("Sanket")#[11, 22, 33, [44, 55, 66, ['raj', 'pavan', 'Sanket']], 77, 88]
print(numbers)

name = ["sanke","Kolhe"]
name.insert(1,"Tularam")#['sanke', 'Tularam', 'Kolhe']
print(name)

l2 = [11,22,33,[44,55,66],88,99]
l2[3].insert(2,888)##[11, 22, 33, [44, 55, 888, 66], 88, 99]
print(l2)

l = [11,22,33,44]
l.remove(22)#[11, 33, 44]
print(l)

l = [11,22,33,[44,55,66,[888,666,552]]]
l[3].remove(44)#[11, 22, 33, [55, 66, [888, 666, 552]]]
print(l)

l2 = [11,22,33,[44,55,66,[888,666,552]]]
l2[3][3].remove(888)#[11, 22, 33, [44, 55, 66, [666, 552]]]
print(l2)

l2[3].remove(66)#[11, 22, 33, [44, 55, [666, 552]]]
print(l2)

name = ["Sanket","Kolhe","Sanket"]
name.pop(2)#['Sanket', 'Kolhe']
print(name)

l = [11,22,44,66]
l.pop()#[11, 22, 44]
print(l)

l2.append(l.pop())#[11, 22, 33, [44, 55, [666, 552]], 44]
print(l2)

l = [111,222,333,444]
l.clear()#[]
print(l)


l = [11,22,33,44]
# del var[index]
del l[1]
print(l)

l2 = [11,22,[44,55]]
l2[2].clear()#[11, 33, 44]
print(l)



l1 = [11,22,33]
l2 = l1#[11, 33, 44]
print(l2)

l2.append(44)
print(l2)#[11, 22, 33, 44]
print(l1)#[11, 22, 33]

l1 = [11,22,33]
l2 = l1.copy()
print(l2)#[11, 22, 33]

