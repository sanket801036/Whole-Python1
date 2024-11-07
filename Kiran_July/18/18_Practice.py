# from abc import *
# class shape:
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radous
#     def area(self):
#         return 3.14*self.radius*self.radius
#     def perimeter(self):
#         return 2*3.14*self.radius
# class square:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return 3.14*self.side*self.side
#     def perimeter(self):
#         return 4*self.side

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print('name: ',self.name)
#         print('age:',self.age)

# class student(person):
#     def __init__(self,name,rollno,marks):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.marks=marks
#     def display(self):
#         print('rollno: ',self.rollno)
#         print('rollno:',self.marks)
#         print('marks:',self.marks)
# s=student('divya',23,85)
#s.display()

class P:
    def __init__(self):
        self.b=20
    def m1(self):
        print("parent instance method")
    @classmethod
    def m2(cls):
        print("parent class method")

    @staticmethod
    def m3():
        print("parent class static method")

class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()




