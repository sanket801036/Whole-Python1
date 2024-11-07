# ### Flow Control Statements
# control the flow of program
# Flow control statements determine the order in which instructions are executed in a program. They can be categorized into conditional statements, iterative statements, and transfer statements.

# #### a. Conditional Statements
# Conditional statements allow the execution of specific blocks of code based on certain conditions.
# 1. `if` Statement
# 2. `if-else` Statement
# 3. `if-elif-else` Statement

# 1. `if` Statement
#   if condition:
#       # code block

#   age = int(input("Enter age: "))
#   if age > 18:
#       print("You are eligible for voting")

# 2. `if-else` Statement
# -

#   if condition:
#       # code block if condition is true
#   else:
#       # code block if condition is false


# 3. `if-elif-else` Statement
# -

#   if condition1:
#       # code block if condition1 is true
#   elif condition2:
#       # code block if condition2 is true
#   else:
#       # code block if no condition is true




# 1. Check Positive Number
# num > 0          to check positive or not
# num < 0          to check negative or not
# num % 2 == 0     to check even or not
# num % 2 != 0     to check odd or not

#    num = eval(input("Enter num: "))
#    if num > 0:
#        print("Positive number")
 

# 2. Check Even Number

#    num = eval(input("Enter num: "))
#    if num % 2 == 0:
#        print("Even number")
 

# 3. Check Negative Number
#    num = eval(input("Enter num: "))
#    if num < 0:
#        print("Negative number")

# 4. Check Odd Number
#    num = eval(input("Enter num: "))
#    if num % 2 != 0:
#        print("Odd number")
 

# #### b. Iterative Statements
# Iterative statements allow the execution of a block of code multiple times.
# 1. Print Only Positive Numbers from a List
#    l = [11, -22, 33, -44, 55, 66]
#    for num in l:
#        if num > 0:
#            print(num)
#      11
#      33
#      55
   
#    Alternative:
#    l = [11, -22, 33, -44, 55, 66]
#    p = [num for num in l if num > 0]
#    print(p)  # [11, 33, 55]
 
# 2. Print Only Negative Numbers from a List
#    l = [11, -22, 33, -44, 55, 66]
#    for num in l:
#        if num < 0:
#            print(num)  
#      -22
#      -44
   
# Alternative:

#    l = [11, -22, 33, -44, 55, 66]
#    p = [num for num in l if num < 0]
#    print(p)  # [-22, -44]
 

# 3. Print Only Even Numbers from a List

#    l = [11, -22, 33, -44, 55, 66]
#    for num in l:
#        if num % 2 == 0:
#            print(num)
 
#    - Output:
   
#      -22
#      -44
#      66
   

#    Alternative:

#    l = [11, -22, 33, -44, 55, 66]
#    p = [num for num in l if num % 2 == 0]
#    print(p)  # [-22, -44, 66]
 

# 4. Print Only Odd Numbers from a List

#    l = [11, -22, 33, -44, 55, 66]
#    for num in l:
#        if num % 2 != 0:
#            print(num)
 
#    - Output:
   
#      11
#      33
#      55
   

#    Alternative:

#    l = [11, -22, 33, -44, 55, 66]
#    p = [num for num in l if num % 2 != 0]
#    print(p)  # [11, 33, 55]
 

# 5. Print Employees with Salary Greater Than 50000

#    employee = {"raj": 22000, "vijay": 51000, "jayesh": 40000, "pavan": 90000}
#    for i in employee:
#        if employee[i] > 50000:
#            print(i)
 
#    - Output:
   
#      vijay
#      pavan
   

# 6. Print Items with Price Greater Than 5000

#    oneplus = {"ce3": 22000, "ce2": 19000, "c24": 24000}
#    for i in oneplus:
#        if oneplus[i] > 5000:
#            print(i)
 
#    - Output:
   
#      ce3
#      ce2
#      c24
   

# #### c. Transfer Statements
# Transfer statements change the flow of execution in a program.



# 1. `break` Statement:
#    - Terminates the loop.

#    for i in range(10):
#        if i == 5:
#            break
#        print(i)
 

# 2. `continue` Statement:
#    - Skips the current iteration and moves to the next.

#    for i in range(10):
#        if i == 5:
#            continue
#        print(i)
 

# 3. `pass` Statement:
#    - Does nothing, can be used as a placeholder.

#    for i in range(10):
#        if i == 5:
#            pass
#        print(i)
 

# These notes provide a concise overview of flow control statements, conditional statements, iterative statements, and transfer statements, along with relevant code examples for quick revision.
