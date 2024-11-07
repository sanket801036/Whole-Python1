#  pickling:   python_obj converted to byte streme called as pickling
#  unpickling: byte streame converted to python object called as unpickling
"""
class employee:
    def __init__(self,id1,name,salary,address):
        self.id=id1
        self.name=name
        self.salary=salary
        self.address=address
    def display(self):
        print("emp id:{},emp_name:{},emp_sal{},emp_add{}".format(self.id,self.name,self.salary,self.address))
emp1 = employee(1, "John Doe", 50000, "123 Elm Street")
emp1.display()

"""
#Sender.py
# sender is responsible to save employee object to file from employee import.
import pickle
class employee:
    def __init__(self,id1,name,salary,address):
        self.id=id1
        self.name=name
        self.salary=salary
        self.address=address
    def display(self):
        print("emp id:{},emp_name:{},emp_sal{},emp_add{}".format(self.id,self.name,self.salary,self.address))
emp1 = employee(1, "John Doe", 50000, "123 Elm Street")
emp1.display()
f=open('emp.txt','wb')
while True:
    eno=int(input("enter employee number:"))
    ename=input("enter employee name:")
    esal=int(input("enter employee sal:"))
    eaddr=input("enter address employee:")
    e=employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
    opetion=input('do you want to serialize one more employee object[yes:no]:')
    if opetion.lower()=='no':
        break
    print("all employee object serialized")

## reciver.py
# reciver is resposible to deserialize employee objects
import pickle
with open('emp.txt','rb') as f:
    print("Deserializing employee objects and printing data")
    while True:
        try:
            obj = pickle.load(f)
            obj.display()
        except EOFError:
            print("All employee objects deserialized")
            break