# area = l*w
# si=(p*r*t)/100
# Simple Interest = (P * R * T) / 100`
# Compound Interest = P * (1 + R/100)^T - P`
#problem 1:Area of Rectangle
#write a python program to calcuate and print the area of a rectangle.Prompt the user to enter the 
#length and width of the rectangle,and then calculate and display the area
l=eval(input("enter lenght:"))
w=eval(input("enter width:"))
area = l*w
print(area)

#Problem 2:-Simple Intrest Calculation
#write a program to calculate and print the simple intrest.Prompt the user to enter the principal
#amount the,the rate of intrest, and the time period.Calculate and display the simple intrest.
p=eval(input("Enter principle value: "))
r=eval(input("Enter Rate: "))
t=eval(input("Enter time period1: "))
si=(p*r*t)/100
print(si)

#problem 4:Perimeter of a Square
#Write a Python program to calculate and print the perimeter of a square,and 
#then calculate and display the perimeter

# s=eval(input("enter the side: "))
# perimete

# Problem 19:- Calculate the total price with tax
#WAP to calculate and print the total price of an item including tax. Prompt the user to enter the 
#price of the item and the tax rate .Calculate and display the total price

price = float(input("Enter the price of the item: "))
tax_rate = float(input("Enter the tax rate (in percentage): "))
tax_amount = price * (tax_rate / 100)
total_price = price + tax_amount

# 5. How do you calculate the total interest for multiple periods in the simple interest formula?

# p = float(input("Enter principal value: "))
# r = float(input("Enter rate: "))
# total_interest = 0
# for i in range(3):  # Example for 3 periods
#     t = float(input(f"Enter time for period {i+1}: "))
#     total_interest += (p * r * t) / 100
# print(f"Total Interest: {total_interest}")
# Explanation: You can use a loop to calculate interest for multiple periods and sum them.
# 7. How can you make the perimeter calculation program handle both square and rectangle inputs?
# python
# Copy code
# shape = input("Enter shape (rectangle or square): ")
# if shape == "square":
#     s = float(input("Enter the side: "))
#     perimeter = 4 * s
# elif shape == "rectangle":
#     l = float(input("Enter length: "))
#     w = float(input("Enter width: "))
#     perimeter = 2 * (l + w)
# else:
#     perimeter = None
#     print("Invalid shape.")
    
# if perimeter:
#     print(f"Perimeter: {perimeter}")
# Explanation: You can handle both square and rectangle calculations by checking the shape type.
# 8. How can you add a feature to the tax calculation program to handle multiple items?
# python
# Copy code
# n = int(input("How many items? "))
# total_price = 0
# for i in range(n):
#     price = float(input(f"Enter price of item {i+1}: "))
#     tax_rate = float(input(f"Enter tax rate for item {i+1}: "))
#     tax_amount = price * (tax_rate / 100)
#     total_price += price + tax_amount

# print(f"Total price for all items: {total_price}")





