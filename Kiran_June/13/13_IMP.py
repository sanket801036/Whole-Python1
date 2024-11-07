#\n new line In Python, \n is a newline character used to insert a new line in a string. It is often used in strings to format text output, making it easier to read or display in a structured way.
# Example 1: Using \n in a single string
greeting = "Hello, World!\nWelcome to Python programming."
print(greeting)
#Hello, World!
# Welcome to Python programming.

# Example 2: Concatenating strings with \n
line1 = "First line"
line2 = "Second line"
line3 = "Third line"
combined_message = line1 + "\n" + line2 + "\n" + line3
print(combined_message)
# First line 
# Second line
# Third line

#\t:-In Python, \t is a tab character used to insert a horizontal tab in a string. It helps to format text output by adding tab spaces, which is useful for creating tabular data or aligning text.
# Example 1: Using \t in a single string
header = "Name\tAge\tLocation"
data = "Alice\t30\tNew York"
print(header)#Name    Age     Location
print(data)  #Alice   30      New York


# Example 2: Concatenating strings with \t
first_column = "First Column"
second_column = "Second Column"
third_column = "Third Column"
formatted_message = first_column + "\t" + second_column + "\t" + third_column
print(formatted_message)#First Column    Second Column   Third Column
print()
#Attributes
#Sep attribute:-In Python, the sep attribute of the print function is used to specify a separator between multiple values. By default, sep is set to a space (' '). You can customize the separator to be any string, such as a comma, a tab, a newline, etc.

# Example 1: Default separator (space)
print("Hello", "World", "Python")#Hello World Python

# Example 2: Using comma as separator
print("Hello", "World", "Python", sep=", ")#Hello, World, Python

# Example 3: Using tab as separator
print("Hello", "World", "Python", sep="\t")#Hello   World   Python**************************************************************************

# Example 4: Using newline as separator
print("Hello", "World", "Python", sep="\n") # *********************************************************************
# Hello
# World
# Python

# Example 5: Using a custom string as separator
print("Hello", "World", "Python", sep=" - ")#Hello - World - Python   ***********************************************

# Example 6: Printing numbers with a separator
print(1, 2, 3, 4, 5, sep=" * ")#1 * 2 * 3 * 4 * 5
print()

for num in range(1,6):
    print(num)#by default \n lag jayenga
# 1
# 2
# 3
# 4
# 5

for num1 in range(1,6):
    print(num1,end=" ")#1 2 3 4 5
print()
name = "raj"
age = "21"
city = "pune"
print("my name is",name,"and",age,"year old and ia am from",city)#my name is raj and 21 year old and ia am from pune
print()

#format():-The format method in Python is used to format strings by inserting specified values into placeholders within the string. Placeholders are defined using curly braces {}. The format method can handle positional arguments, keyword arguments, and more complex formatting.
#Basic Usage
# Example 1: Positional arguments
g = "Hello, {}. Welcome to {}!"
f = g.format("Alice", "Wonderland")
print(f)  # Output: Hello, Alice. Welcome to Wonderland!

# Example 2: Keyword arguments
g = "Hello, {name}. Welcome to {place}!"
f = g.format(name="Alice", place="Wonderland")
print(f)  # Output: Hello, Alice. Welcome to Wonderland!
print()

#Positional and Keyword Arguments

# Example 3: Mixed positional and keyword arguments
g = "Hello, {0}. Welcome to {1}! Enjoy your stay, {0}."
f = g.format("Alice", "Wonderland")
print(f)  # Output: Hello, Alice. Welcome to Wonderland! Enjoy your stay, Alice.

# Example 4: Reusing arguments
g = "Hello, {name}. Welcome to {place}! Enjoy your stay, {name}."
f = g.format(name="Alice", place="Wonderland")
print(f)  # Output: Hello, Alice. Welcome to Wonderland! Enjoy your stay, Alice.
print()

# Formatting Numbers
# Example 5: Formatting integers
n = "The number is: {:d}"
f = n.format(42)
print(f)  # Output: The number is: 42

# Example 6: Formatting floats with precision
n = "The price is: {:.2f}"
f = n.format(19.99)
print(f)  # Output: The price is: 19.99
print()

#Padding and Alignment****************************************************************************************
# Example 7: Padding and aligning text
text = "|{:<10}|{:^10}|{:>10}|"
formatted_text = text.format("left", "center", "right")
print(formatted_text)  # Output: |left      |  center  |     right|

# Example 8: Padding with a specific character
text = "|{:-^10}|"
formatted_text = text.format("centered")
print(formatted_text)  # Output: |centered-|

#Complex Formatting
# Example 9: Formatting with nested placeholders
item = "Item: {name}, Price: ${price:.2f}, Quantity: {quantity}"
formatted_item = item.format(name="Apple", price=0.99, quantity=5)
print(formatted_item)  # Output: Item: Apple, Price: $0.99, Quantity: 5

# Example 10: Using dictionaries with the format method
data = {"name": "Alice", "place": "Wonderland"}
greeting = "Hello, {name}. Welcome to {place}!"
formatted_greeting = greeting.format(**data)
print(formatted_greeting)  # Output: Hello, Alice. Welcome to Wonderland!
# In these examples:

# Positional and keyword arguments demonstrate the flexibility of the format method.
# Number formatting shows how to format integers and floating-point numbers.
# Padding and alignment examples demonstrate text alignment and padding within a specified width.
# Complex formatting examples show how to handle nested placeholders and use dictionaries with the format method.
# The format method is very powerful and can handle a wide range of formatting tasks, making it a versatile tool for creating formatted strings in Python.

name = "raj"
age = 21
city = "pune"
print("my name is {n} i am {a} year old and i am from {c}".format(a=age,c = city,n=name))#my name is raj i am 21 year old and i am from pune
print()
print()

#************f"":-****************************

#The `f-string` in Python is a more modern and efficient way to format strings compared to the `format()` method. It allows you to embed expressions within the string using curly braces `{}`. Here's how you can use `f-strings` in the provided code:

#print(f"msg{var}msg{var}")
name  = "raj"
city  = "pune"
print(f"my name is {name} and ia am from {city}")#my name is raj and ia am from pune

car = {"car":{"bmw":{"x1","x2","x3","x4"}},"color":"blue","model":"bvv"}
car["car"]["bmw"].add("x5")
print(car)#{'car': {'bmw': {'x1', 'x4', 'x3', 'x5', 'x2'}}, 'color': 'blue','model': 'bvv'}




# Example 1: Using f-string in a single string
g = f"Hello, World!\nWelcome to Python programming."
print(g)
#Hello, World!
# Welcome to Python programming.

# Example 2: Concatenating strings with f-string
line1 = "First line"
line2 = "Second line"
line3 = "Third line"
combined_message = f"{line1}\n{line2}\n{line3}"
print(combined_message)
# First line 
# Second line
# Third line

# Example 3: Using f-string with tab character
header = f"Name\tAge\tLocation"
data = f"Alice\t30\tNew York"
print(header)
#Name    Age     Location
print(data)  
#Alice   30      New York

# Example 4: Concatenating strings with f-string and tab character
first_column = "First Column"
second_column = "Second Column"
third_column = "Third Column"
formatted_message = f"{first_column}\t{second_column}\t{third_column}"
print(formatted_message)
#First Column    Second Column   Third Column

# Example 5: Printing variables with f-string
name = "raj"
age = 21
city = "pune"
print(f"my name is {name} and {age} year old and i am from {city}")
#my name is raj and 21 year old and i am from pune

# Example 6: Printing expressions with f-string
num = 42
print(f"The square of {num} is {num**2}")
#The square of 42 is 1764

# Example 7: Using f-string with conditional expressions
is_valid = True
print(f"The result is {'valid' if is_valid else 'invalid'}")
#The result is valid

# Example 8: Using f-string with dictionary
data = {"name": "Alice", "place": "Wonderland"}
greeting = f"Hello, {data['name']}. Welcome to {data['place']}!"
print(greeting)
#Hello, Alice. Welcome to Wonderland!

#In these examples, you can see how `f-strings` provide a more concise and readable way to format strings in Python. They can be used to embed variables, expressions, conditional expressions, and dictionaries directly within the string.

#1)Calculate the interest on a savings account based on the balance and account type. 
#Problem Statement: Calculate the annual interest on a savings account based on the balance and account type. The interest rates are: 3% for regular accounts with balances up to $10,000, 4% for regular accounts with balances up to $10,000, 4% for regular accounts with balances over $10,000, and 5% for premium accounts.
#i=p*r*t
# a=(input("enter the account type: "))
# b=eval(input("enter the account balance: "))
# if a=="regular" and b>10000:
#     bal=b/100*3
#     print(bal+b)
#OR
# b = 5000
# a = "regular"
# if a == "regular" and b <= 10000:
#     i = 3
# elif a == "regular" and b > 10000:
#     i = 4
# elif a == "premium":
#     i = 5
# else:
#     print("Invalid account type or balance")
# i = b*i/100
# print(f"The annual interest on a {a} account with a balance of {b} is {i:.2f}.")

#2)Determine the type of triangle based on side lengths. Problem Statement: Determine the type of triangle based on the lengths of its sides. The types are: Equilateral if all sides are equal, Isosceles if exactly two sides are equal, and Scalene if all sides are different.
s1=input("enter side 1 of triangle :")
s2=input("enter side 1 of triangle :")
s3=input("enter side 1 of triangle :")

if s1==s2==s3:
    print("Equilateral triangle")
elif s1==s2 or s3==s2 or s1==s3:
    print("isoceles triangle")
else:
    print("Scalene triangle")

#3)Determine the type of fruit based on color and size.
#Problem Statement: Determine the type of fruit based on its color and size. The fruits are: 'apple' if red and medium-sized, 'banana' if yellow and long, 'cherry' if red and small, and 'grape' if green and small.
color = input("Enter the color of the fruit: ")
size = input("Enter the size of the fruit: ")
if color == "red" and size == "medium-sized":
    print("The fruit is apple")
elif color == "yellow" and size == "long":
    print("The fruit is banana")
elif color == "green" and size == "long":
    print("The fruit is grape")
else:
    print("Invalid input")

