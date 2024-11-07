# l=[11,22,33,44,55,66]
# iter_obj=iter(l)
# #iter() get an iterator from an object
# print(iter_obj)
# print(next(iter_obj))#11
# #next() return next item from an iterator
# print(next(iter_obj))#22
# print(next(iter_obj))#33
# print(next(iter_obj))#44
# print(next(iter_obj))#55
# print(next(iter_obj))#66
# print(next(iter_obj))#StopIteration

# l=[11,22,33,44,55,66]
# iter_obj=l._iter_()
# print(next(iter_obj))#11
# print(next(iter_obj))#22
# print(next(iter_obj))#33
# print(next(iter_obj))#44
# print(next(iter_obj))#55
# print(next(iter_obj))#66
# try:
#     print(next(iter_obj))#StopIteration
# except:
#     print("no element left ")

# l=[11,22,33,44,55,66]
# iter_obj=iter(l)
# print(dir(l))# there is _iter_ available so it is iterable
# print(dir(iter_obj))#here _iter_ and '_next_  is available then it is iterator


# def myforloop(iterable):
#     iter_obj=iter(iterable)
#     while True:
#         print(next(iter_obj))
# print(myforloop([1,2,3,4,5,6]))#StopIteration


# def myforloop(iterable):
#     iter_obj=iter(iterable)
#     try:
#         while True:
#             print(next(iter_obj))
#     except StopIteration:
#         pass