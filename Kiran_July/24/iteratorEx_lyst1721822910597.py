# l=[11,22,33,44,55]
# #iter():=>Get an iterator from an iterable#
# iter_obj=iter(l)
# print(iter_obj)
# #next()=>Return the next item from the iterator.
# print(next(iter_obj)) #11
# print(next(iter_obj)) #22
# print(next(iter_obj)) #33
# print(next(iter_obj)) #44
# print(next(iter_obj)) #55
# # print(next(iter_obj)) #StopIteration



# l=[1,2,3,4,5]#jiske upper for loop lgta hai usko iterable kahate hai  
# #how to make iterator(iter_object) of the list
# iter_obj=iter(l)
# for num in iter_obj:
#     print(num)#for loop is working so every iterator is iterable

#iteration :-iteration ek proccess hai jiska kam hai ek ek element ko bahar nikalana
#iterator and iterable
#iterable
# l=[11,22,33,44,55]
# # only '__iter__'  method
# print(dir(l)) #Show attributes of an object.
# #iterator 
# iter_obj=iter(l)
#__next__ and __iter__ method
# print(dir(iter_obj))



# l=[11,233,44,55]
# iter_obj=l.__iter__()
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# print(iter_obj.__next__())

# n="sarvesh"
# # print(dir(n))
# iterator=n.__iter__()
# print(dir(iterator))
# iterator1=iterator.__iter__()
# print(id(iterator))
# print(id(iterator1))



#iter_obj=>iter()   next()

# l=[11,22,33]
# def myfor(iterable):
#     iter_obj=iter(iterable)
#     try:
#         while True:
#             print(next(iter_obj))
#     except StopIteration:
#         pass

# d={"name":"rahul","age":21,"city":"pune"}
# myfor(d)


# r=range(1,6,1)  #__iter__ ## iterable
# for i in r:
#     print(i)


class myrange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):#RANGE FUNCTION KE dir ke andar __iter__ rahati hai usko ko bhi involve krna honga#ismein next nhi hoti to bananeki jrurat nhi
        return myrangeiterator(self)#iter method iterator ka object return me deti thi so isko bhi return krna honga

class myrangeiterator:#range ka khudka iterator(iter_obj) hota hai so iska bi banana honga
    def __init__(self,myrange_obj):#jaise renge mei value get krta hai range ki vasehi yaha pr bhi lagenga 
        self.myrange_obj=myrange_obj
    def __iter__(self):#iterator ka iter khudko return krta hai
        return self
    def __next__(self):
        result=self.myrange_obj.start
        if self.myrange_obj.start<self.myrange_obj.end:
            self.myrange_obj.start=self.myrange_obj.start+self.myrange_obj.step
            return result
        else:
            raise StopIteration





for i in myrange(2,1000,100):
    print(i)




