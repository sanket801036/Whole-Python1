#try exception**********************
#it include :
# try:
#     #body of except#the code in which we think error may occur
#     #risky

# except:
#     #body of except#in this we write the code in which we  handele exception
#     #code to handel exception
# else:#eception nhi ata hai to else block execute honga
#     pass
#finally:#always execut karnege

n1=eval(input("n1: "))
n2=eval(input("n2: "))
try:
    div=n1/n2
    print(div)
except:
    print("you can't divide number by zer0")

# n1=eval(input("n1: "))
# n2=eval(input("n2: "))
# mul=n1*n2
# sum=n1+n2
# sub=n1-n2
# try:
#     div=n1/n2 
# except:
#     print("you can't divide number by zer0")
# else:
#     print(div)
# finally:
#     print(mul)
#     print(sum)
#     print(sub)



# n1=10
# n2=5
# try:
#     div=n1/n2
#     print(div)
# except ZeroDivisionError as e:
#     print(e)
# except NameError as e:
#     print(e)

n1=10
n2=0
try:
    div=n1/n2
    print(div)
except Exception as e:
    print(e)