# a = 3.14*r*r
# s = d/t
# A = (a+b+c)/3
# ta = p*(1+(r/n))**n*t
# v = (4/3)*3.14*(r**3)



r = (eval(input("Enter the radius: ")))
a = 3.14*r*r
print(a)

d = eval(input("Enter distance in km: "))
t = eval(input("Enter the time: "))
s = d/t
print("The speed is: ",s)

a = eval(input("Enter first no.: "))
b = eval(input("Enter second no.: "))
c = eval(input("Enter third no, "))
A = (a+b+c)/3
print(A)

#Problem 4:Calculate Compound Intrest
#wap to calculate and print the compound intrest.Prompt the user to enter the principle amount,the rate
#of intrest is compoinded per year, and the time period(in years).
#eCalculate and display the compound intrest

p = eval(input("Enter the principal amount: "))
r = eval(input("Enter the rate of intrest: "))
n = eval(input("no of times intrest compound per year:"))
t = eval(input("Enter the time period: " ))
dr = r/100
ta = p*(1+(r/n))**n*t
ci = ta-p
print(ci)

#Problem 5: Volume of sphere
#WAP to calculate and print the volume of a sphere, and then calculate and display the volume.
r = eval(input("Enter the radius: "))
v = (4/3)*3.14*(r**3)  #if you want to square it then write(r**2),fot cube(r**3).....etc
print("Valume of the sphera is: ",v)

#Pro 6 *********************************************************************************************************************
p = eval(input("what is price of product: "))
d = eval(input("Discount available: "))
tm = p*(d/100)
amount = p- tm
print("Your total amount is: ",amount)

# Sure! Here are the explanations and formulas for each code snippet provided:
r = eval(input("Enter the radius: "))
a = 3.14 * r * r
print(a)
# Output:
# Enter the radius: 5
# 78.5


# ### 2. Calculate the Speed
# Concept:
# Speed is the distance traveled divided by the time taken to travel that distance.

d = eval(input("Enter distance in km: "))
t = eval(input("Enter the time: "))
s = d / t
print("The speed is: ", s)

# Enter distance in km: 100
# Enter the time: 20
# The speed is:  5.0


# ### 3. Calculate the Average of Three Numbers
a = eval(input("Enter first no.: "))
b = eval(input("Enter second no.: "))
c = eval(input("Enter third no, "))
A = (a + b + c) / 3
print(A)

# Output:
# Enter first no.: 10
# Enter second no.: 20
# Enter third no, 30
# 20.0


# ### 4. Calculate Compound Interest
# Formula:
# Concept: Compound interest is calculated on the principal amount plus the interest that has been added to it over time. The formula accounts for the number of times the interest is compounded per year.
p = eval(input("Enter the principal amount: "))
r = eval(input("Enter the rate of interest: "))
n = eval(input("No. of times interest compounded per year: "))
t = eval(input("Enter the time period: "))
dr = r / 100
ta = p * (1 + (dr / n))  (n * t)
ci = ta - p
print(ci)

# Enter the principal amount: 1000
# Enter the rate of interest: 5
# Enter no of times interest compound per year: 12
# Enter the time period: 2
# 105.12710963760242


# ### 5. Calculate the Volume of a Sphere
# The volume of a sphere is calculated using the radius (r) and the constant π (pi).
r = eval(input("Enter the radius: "))
v = (4 / 3) * 3.14 * (r**3)
print("Volume of the sphere is: ", v)
# Enter the radius: 3
# Volume of the sphere is:  113.09733552923255

# ### 6. Calculate the Total Amount After a Discount
# The total amount after a discount is calculated by subtracting the discount amount from the original price.
p = eval(input("What is the price of the product: "))
d = eval(input("Discount available: "))
tm = p * (d / 100)
amount = p - tm
print("Your total amount is: ", amount)

# What is the price of the product: 1000
# Discount available: 20
# Your total amount is:  800.0


