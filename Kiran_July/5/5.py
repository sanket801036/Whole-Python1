class Employee:
    #class/static variable
    company='TKA'
    location = 'karve nagar'
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
    # classmethod
    @classmethod
    def company_details(cls):
        print(f"company name:{cls.company}\nLocation:{cls.location}")
e1=Employee("vijay","nashik","mr",34000)
e1.details()#to call the instance 
e2=Employee("ajay","nagpur","hr",54000)
e2.details()#to call the instance        
#you can also get access by using class name
Employee.company_details()