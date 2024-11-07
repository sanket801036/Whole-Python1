# 1)what is set?
# Ser:-Set is a comma separated value within {}
# Syntax:- var_name{val1,val2,...}
# Defination:-it is unorder,mutable,heterogeneous collection immutable elements where insertion order
# is not preserved and duplicate is not allowed

# Unoerdered:- Index not present
# Mutable:-Changeable.
# Heterogeneous collection of immutable elements:-we can add int,string, float,bool,float data into set

# 2)How to create empty set:-
# by using class s = set()

# Problem 19:- Calculate the total price with tax
# #WAP to calculate and print the total price of an item including tax. Prompt the user to enter the  price of the item and the tax rate .Calculate and display the total price

price = float(input("Enter the price of the item: "))
tax_rate = float(input("Enter the tax rate (in percentage): "))
tax_amount = price * (tax_rate / 100)
total_price = price + tax_amount
