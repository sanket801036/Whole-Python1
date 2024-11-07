#*************Student Management System ****************
db={1:{"name":"sanket","city":"pune","percentage":89}}
print("-"*100)
print(f"{' '*40} The Kiran Academy")
print("-"*100)
while True:
    print(f""" 
    {' '*30} Dashboard
    {' '*25}1.Add Student Details
    {' '*25}2.Display Student Details
    {' '*25}3.Update Student Details
    {' '*25}4.Display Student Details
    """)
    ch = int(input("Enter your choice: "))
    if ch==1:
        details={}
        roll=int(input("Enter roll number: "))
        name = input("enter Name : ")
        city = input("enter City : ")
        per=eval(input("Enter Percents : "))
        details["name"]=name
        details["city"]=city
        details["percentage"]=per
        db[roll]=details
        
    elif ch==2:
        print("-"*86)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Roll No","Name","City","Percentage"))
        print("-"*86)
        if len(db)>0:
                
            for roll in db:
                print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll,db[roll]['name'],db[roll]['city'],db[roll]['percentage']))
                print("-"*86)
        else:
            print("-"*86)
            print("No data found: ")
            print("-"*86)
    elif ch==3:
        r=int(input("enter roll no: "))
        if r in db:
            print("""
            1.Name
            2.City
            3.percentage
            """)
            ch=int(input("enter choice: "))
            if ch==1:
                un=input("name: ")
                db[r]["name"]=un
                print("update...")
            elif ch==2:
                uc=input("city: ")
                db[r]["city"]=uc
                print("updated...")
            elif ch==3:
                up=input("percentage: ")
                db[r]["percentage"]=up
                print("updated...")
            else:
                print("Invalid")
        else:
            print("Invalid")

    elif ch==4:
        r=int(input("enter roll No: "))
        if r in db:
            db.pop(r)
        else:
            print("invalid roll number")
    elif ch==5:
        print("Invalid Input...")

