# Loop Task

# control flows

# 1) Conditional statements:-  if else

# 2) iterative loop:- 
#    for, while

# 3) branching statements:- 
#    switch case

# if else

#Task 1:-To display profit and lost
# selling price - 1500
# cost price    - 1000

# cost=int(input("Enter the cost of the product: "))
# sell=int(input("Enter the selling price of the product: "))
# if sell>cost:
#     print("You have made the profit")
# elif sell<cost:
#     print("You have made the loss")
# else:
#     print("Not a profit Not a loss")


#2)To enter basic salary from user, hra(house rent allowance) will be 10% of bs
# bonus = 2400
# otherwise hra will be 5% of bs
# ta(travaling allowance) = 1000
# bonus = 1500
# then calculate netsal of employee
# netsal = bs+hra+ta+bonus

bs=int(input("Enter basic sallary: "))
if bs>=10000:
    hra=(10/100)*bs
    ta=bs*5/100
    bonus=2400
else:
    hra=bs*5/100
    ta=1000
    bonus=1500

netsal = bs+hra+ta+bonus
print(netsal)

#3)write a program to find the eligibility of admission for a professional course based on the following criteria:
# Marks in Maths             >=65
# Marks in Phy               >=55
# Marks in Chen              >=50
# Total in all three subject >=180

maths = int(input("Enter marks in Maths: "))
phy = int(input("Enter marks in Physics: "))
chem = int(input("Enter marks in Chemistry: "))
total = maths + phy + chem

if maths >= 65 and phy >= 55 and chem >= 50 and total >= 180:
    print("Eligible for admission")
else:
    print("Not eligible for admission")

#4) Write a python program to input any alphabet and check wheather it is vowel or consonant.
alphabet = input("Enter an alphabet: ")

if alphabet.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{alphabet} is a vowel")
else:
    print(f"{alphabet} is a consonant")

#5)Write a python program to check number is divisible by 3 ir 5.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5")
elif number % 3 == 0:
    print(f"{number} is divisible by 3")
elif number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 3 or 5")
