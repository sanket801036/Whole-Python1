db = {1: "poha", 2: "samosa", 3: "upama", 4: "dosa", 5: "kachori", 6: "vadapav"}
price = {1: 20, 2: 15, 3: 20, 4: 50, 5: 15, 6: 15}
item = []
qu = []

print("-" * 100)
print(" " * 30 + "Garibowala Hotel")
print("-" * 100)
i=1
print("""
            Menu
    1. Poha        4. Dosa
    2. Samosa      5. Kachori
    3. Upama       6. Vadapav
""")

while True:
    i = int(input("Enter your choice: "))
    q = int(input("Enter your quantity: "))
    item.append(i)
    qu.append(q)
    c = input("Do you want to continue (y/n): ")
    if c == "n":
        print("-"*105)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("sr no","Item","Quantity","Price","Amount"))
        print("-"*105)
        sum=0
        for i in range(len(item)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i+1,db[item[i]],qu[i],price[item[i]],price[item[i]],price[item[i]]*qu[i]))
            print("-"*105)
            sum=sum+price[item[i]]*qu[i]
        print(f"Yur Total amount is {sum}")
        break
    i=i+1

#HW:-give discoun 2% and add column of discount also