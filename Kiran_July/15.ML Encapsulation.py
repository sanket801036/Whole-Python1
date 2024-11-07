#Encapsulation
# It refers to the bundling of data and methods that operate on that data into a single unit,called a class .Encapsulation allows you to hide the internal state of an object.
class Counter:
    def __init__(self):
        self.count=0
    def inc(self):
        self.count=self.count+1
    def dec(self):
        self.count=self.count-1
    def check(self):
        print(f"count {self.count}")

c=Counter()
print(c.count)
c.inc()
c.inc()
c.check()#count 2
print(c.count)
c.count=999
print(c.count)#999 #apan isko(public variable ko) bahar access bhi kr pa rhe hai our change bhi kr pa rhe hai to stop this we sometimes some data need to be private so we use encapsulation here

class Counter:
    def __init__(self):
        self.__count=0  #Private
    def inc(self):
        self.__count=self.__count+1
    def dec(self):
        self.__count=self.__count-1
    def check(self):
        print(f"count {self.__count}")

c=Counter()
c.inc()
c.inc()
c.inc()
c.inc()
c.inc()
c.inc()
c.dec()
c.check()#count 5
#print(c.count)#'Counter' object has no attribute 'count'#abb acces nhi kr paha rhe hai due to we make it private by giving two under score like __count
#print(c.__count)# 'Counter' object has no attribute '__count'#aab accsess nhi kr pa rahe
# c.__count=999
#c.check()#'Counter' object has no attribute '__count'# aab apan chenge bhi nhi kr pa rhe 

class Finance:
    def __init__(self):
        self.revenue=100000
        self.days=10
    def check_revenue(self):
        print(f"revenue is {self.revenue} in {self.days} days")

f=Finance()
d=f.check_revenue()#revenue is 100000 in 10 days

class Hr:
    def __init__(self):
        self.no_of_emp=10
        print(f.revenue)
        f.revenue=0#aab revenue apan ne change kr diya hai 0 kr diya hai

h=Hr()#100000 #finance class ke revenue variable ho apan Hr clas ke acces kr pa rha hai
#publick variable ho outside of the class bhi access kr skte hai aur inside of the class bhi kr skte hai
f.check_revenue()#revenue is 0 in 10 days # ha apan inside of the class punlic variable ko change bhi kr skte hai

print("aab usko private banayenge(by giving two underscore) check krenge acces kr skte hai kya? aur change kr skte hai kya? aise")

class Finance:
    def __init__(self):
        self.__revenue=100000
        self.days=10
    def check_revenue(self):
        print(f"revenue is {self.__revenue} in {self.days} days")

f=Finance()
d=f.check_revenue()#revenue is 100000 in 10 days

class Hr:
    def __init__(self):
        self.no_of_emp=10
        print(f.revenue)#'Finance' object has no attribute 'revenue'# abb isko apan access nhi kr pa hai hai
        f.revenue=0#aab revenue apan ne change kr diya hai 0 kr diya hai

h=Hr()
f.check_revenue()#AAB usko change bhi ni kr sk rahe hai