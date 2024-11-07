db = {1: "Milk", 2: "Bread", 3: "Rice", 4: "Sugar", 5: "Salt", 6: "Butter"}
price = {1: 50, 2: 30, 3: 60, 4: 40, 5: 20, 6: 80}
item = []
qu = []

print("-" * 100)
print(" " * 30 + "DMart Shopping")
print("-" * 100)
print("""
            Menu
    1. Milk        4. Sugar
    2. Bread       5. Salt
    3. Rice        6. Butter
""")

while True:
    i = int(input("Enter your choice: "))
    q = int(input("Enter your quantity: "))
    item.append(i)
    qu.append(q)
    c = input("Do you want to continue shopping (y/n): ")
    if c.lower() == "n":
        print("-" * 125)
        print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Sr No", "Item", "Quantity", "Price", "Amount"))
        print("-" * 125)
        total_amount = 0
        for idx in range(len(item)):
            amount = price[item[idx]] * qu[idx]
            total_amount += amount
            print("|{:^10}|{:^20}|{:^20}|{:^20}|{:^20}|".format(
                idx + 1, db[item[idx]], qu[idx], price[item[idx]], amount))
            print("-" * 125)
        print(f"Your total amount is {total_amount}")
        break
