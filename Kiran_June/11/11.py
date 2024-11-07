# GIves the 10% dicount if value  is greater than 22000 else 5%
vivo={"v15":13000,"v16":25000,"v20":19000,"v21":27000}
for model in vivo:
    if (vivo[model]>22000):
        vivo[model]=vivo[model]-(vivo[model]*(10/100))
    else:
        vivo[model]=vivo[model]-(vivo[model]*(5/100))
print(vivo)

#Wap
n=eval(input("Enter your marks: "))
students={"ram":70,"sita":80,"laxman":90,"ravan":60}
for marks in students:
    if (students[marks]>70):
        students[marks]="B+"
    elif(students[marks]>80):
        students[marks]="B+"
    elif(students[marks]>90):
        students[marks]="A+"
    elif(students[marks]>60):
        students[marks]="B"
    else:
        print("F")


num1=eval(input("Enter a number: "))
operator=input("which operator: ")
num2=eval(input("Enter a second number: "))

if operator:
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    elif operator=="%":
        print(num1%num2)
    elif operator=="//":
        print(num1//num2)
    elif operator=="**":
        print(num1**num2)
    else:
        print("Invalid operator")
  
# n=eval(input("Enter number: "))
# if n==1:
#     print("janevary")
# elif n==2:
#     print("february")
# elif n==3:
#     print("march")
# elif n==4:
#     print("april")
# elif n==5:
#     print("may")
# elif n==6:
#     print("june")
# elif n==7:
#     print("july")
# elif n==8:
#     print("august")
# elif n==9:
#     print("september")
# elif n==10:
#     print("october")
# elif n==11:
#     print("november")
# else:
#     print("december")    

# age=eval(input("Enter your age: "))
# if age>60:
#     print("Senior citizen")
# elif age>70:
#     print(" Super Senior citizen")
# elif age>18:
#     print("full age citizen")
# elif age>12:
#     print("Minor citizen")
# elif age<12:
#     print("Your are kid")
# else:
#     print("You are child")

# vishal=21
# arun=24
# vijay=22
# if vishal>arun and vishal>vijay:
#     print("Vishal")
# elif vishal>arun and arun>vijay:
#     print("arun")
# else:
#     print("vijay")


# d=eval("enter a shipping type: ")
# w=input("wheight: ")
# if d=='domestic':
#     if w<=5:
#         print("code is 10")
#     elif w<20:
#         print("cose is 20")
#     else("cost is 30")
# elif d='international':
#     if w<=5:
#         print("code is 15")
#     elif w<=20:
#         print("cose is 50")
#     else:
#         print()


    

