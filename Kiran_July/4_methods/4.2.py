
class Employee:
    def __init__(self,name,city,dep,sal):
        self.name = name                    #instance variable
        self.city = city                    #instance variable
        self.dep = dep                      #instance variable
        self.sal = sal                      #instance variable
    def details(self):                      #instance method
        print(f"""
                Name:{self.name} 
                City:{self.city}
                Department:{self.dep}
                Salary :{self.sal}
                
                """)                        #instance method

e1=Employee("raj","pune","HR",23000)
e1.details()      