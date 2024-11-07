#1.wap to enter two integers and then performs all arithmetic operation
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

print("Addition of num1 and num2",add)
print("Substraction of num1 and num2",sub)
print("Multiplication of num1 and num2",multi)
print("Division of num1 and num2",division)
print("modulus of num1 and num2",modulus)
print("Exponentiation of num1 and num2:", exponentiation)
print("Floor division of num1 and num2:", floor_division)

# 2.)Repeat the program using floating point numbers
num1 = float(input("Enter the first floating point number: "))
num2 = float(input("Enter the second floating point number: "))
add = num1 + num2
sub = num1 - num2
multi = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

print("Addition of num1 and num2:", add)
print("Subtraction of num1 and num2:", sub)
print("Multiplication of num1 and num2:", multi)
print("Division of num1 and num2:", division)
print("Modulus of num1 and num2:", modulus)
print("Exponentiation of num1 and num2:", exponentiation)
print("Floor division of num1 and num2:", floor_division)

#Write a program to perform string cocatnation

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

concatenated_str = str1 + str2
print("Concatenated string:", concatenated_str)

#4)write a program to demonstrate printing a string within single quotes, double quotes, 
#and triple quotes

single_quotes_str = 'This is a string enclosed in single quotes'
double_quotes_str = "This is a string enclosed in double quotes"
triple_quotes_str = '''This is a string enclosed in triple quotes'''

print("Single quotes string:", single_quotes_str)
print("Double quotes string:", double_quotes_str)
print("Triple quotes string:", triple_quotes_str)

#5)WAP program to print the ASCII value of acharacter
character = input("Enter a character: ")
ascii_value = ord(character)
print(ascii_value)

#6.write a program to read a character in uppercase amd then  print it in lowercase
character = input("Enter a character in uppercase: ")
lowercase_character = character.lower()
print("Character in lowercase:", lowercase_character)

#7.write a program to swap two numbers using temporary variable
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
temp = num1
num1 = num2
num2 = temp
print("First number:", num1)
print("Second number:", num2)

#8.write a program to demonstrate implicit conversion
c = 1.9
d = 8 #python convert int to float automatically
print(c + d)

#9.write a program to to demonstrate explicit conversion
a = "1"
b = "2"
print("int(a)+int(b)") #we convert string to int
print("-------------10-------------------")

#10) wap to read the address of a user.Display the result by breaking it in multiple lines
address = input("Enter your address: ")
address_lines = address.split(',')
print("Address:")
for line in address_lines:
    print(line.strip())

# 11) Write a program to read two floating point numbers. Add these numbers and assign the
#  result to an integer
num1 = float(input("Enter the first floating-point number: "))
num2 = float(input("Enter the second floating-point number: "))

result = int(num1 + num2)
print("The sum of the two numbers, rounded to the nearest integer, is:", result)

# 12) Write the python program to calculate simple intrest and compound intrest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
n = 1
compound_interest = principal * (pow((1 + rate / (n * 100)), (n * time)) - 1)
print("Compound Interest:", compound_interest)

#13) write the program that prompts user to enter two integers x and y. The program then
# then calculates the and displays x
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
sum_result = x + y
print("The sum of is", sum_result)

#14) write the program that prompts user to enter his first name and last name and 
# then displays a message "Greetings!!! First name Last name".
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Greetings!!! " + first_name + " " + last_name)

#15) write a program to calculate salary of an employee given his basic pay
# (to be entered by the user), HRA 10 per cent of basic pay, TA = 5 per cent of basic
#  pay. Define HRA and TA as constants and use them to calculate the salary of the 
# employee.

basic = float(input("Enter the basic pay: "))
hra = (basic*10)/100
ta = (basic*5)/100
salary = basic + hra + ta
print("Salary is:", salary)

#to print hra and ta
print("HRA = ",hra)
print("TA = ", ta)

#16) write a program to prepare grocery bill.For that enter the name of the items purchased,
#quantity in which it is purchased, and its price per unit. Then display the bill in the
#following format.

# **********BILL**********
# Item Name Item Quantity Item Price amount
# Total amount to be paid=

# Prepare Grocery Bill

# Initialize variables
total_amount = 0

# Print bill header
print("**********BILL**********")
print("Item Name\tItem Quantity\tItem Price\tAmount")

# Get item details from user
while True:
    item_name = input("Enter the name of the item (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_quantity = int(input("Enter the quantity of the item: "))
    item_price = float(input("Enter the price per unit of the item: "))
    # Calculate amount for the ite
    item_amount = item_quantity * item_price
    # Print item details and amount
    print(f"{item_name}\t\t{item_quantity}\t\t{item_price}\t\t{item_amount}")
    # Update total amount
    total_amount += item_amount
# Print total amount to be paid
print(f"Total amount to be paid: {total_amount}")

#17)Momentum is calculated as, e = mc^2(means (mc)square), where m is the mass of the object and
# c is its velocity. write a program that accepts an objects mass (in kilograms)and velocity
# (in meters per second)and displays its momentum.
mass = float(input("Enter the mass of the object (in kilograms): "))
velocity = float(input("Enter the velocity of the object (in meters per second): "))
# Calculate momentum using the formula e = mc^2
momentum = mass * velocity**2
# Display the calculated momentum
print("The momentum of the object is:", momentum, "kg*m^2/s^2")

#18) write a program that calculates number of seconds in a day.
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
seconds_in_day = seconds_in_minute * minutes_in_hour * hours_in_day
print("Number of seconds in a day:", seconds_in_day)




