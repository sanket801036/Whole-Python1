"""#Which of 
# x=int(43.55+2/2)
# print(x)#44

#Which of the following is not a complex numk
#
#2)Which of the following is operator has its associativity from left to right
#a. +   b. //   c. %   d. **
# the associativity of operators determines how operators with the same precedence are grouped together. Operators with left-to-right associativity are evaluated from left to right, while operators with right-to-left associativity are evaluated from right to left.
Here are the operators mentioned with their associativity:
a. + (Addition): Left-to-right associativity.
Example:
x = 4 + 3 + 2  # Evaluated as (4 + 3) + 2 = 9
print(x)  # Output: 9

b. // (Floor division): Left-to-right associativity.
Example:
x = 10 // 3 // 2  # Evaluated as (10 // 3) // 2 = 1
print(x)  # Output: 1

c. % (Modulo): Left-to-right associativity
Example:
x = 10 % 3 % 2  # Evaluated as (10 % 3) % 2 = 1
print(x)  # Output: 1

d. ** (Exponentiation): Right-to-left associativity.*************************************************
Example:
x = 2 ** 3 ** 2  # Evaluated as 2 ** (3 ** 2) = 2 ** 9 = 512
print(x)  # Output: 512
In summary, the operator with its associativity from left to right is:

a. + (Addition)
The other operators mentioned do not have their associativity from left to right. The exponentiation operator (**) has right-to-left associativity.

# 3) What is the maximum possible length of an identifier?
# A)31 characters
# B)63 characters
# C)79 characters
# D)none of the mentioned#but answer is D
The maximum possible length of an identifier in Python is determined by the implementation and the available memory. However, there is a practical limit due to the maximum length of a string in Python.
A) 31 characters(is ans): This is not the maximum possible length. Python allows identifiers to have a maximum length of approximately 31 characters.

B) 63 characters: This is not the maximum possible length. Python allows identifiers to have a maximum length of approximately 31 characters.

C) 79 characters: This is not the maximum possible length. Python allows identifiers to have a maximum length of approximately 31 characters.

D) None of the mentioned: This option is incorrect. Python does allow identifiers to have a maximum length of approximately 31 characters.

In Python, the maximum length of an identifier is determined by the implementation and the available memory. The actual maximum length can vary depending on the Python interpreter and the system's memory constraints. However, it is generally recommended to keep identifier names short and meaningful to improve code readability.

If you need a longer identifier, you can use a combination of letters, numbers, and underscores, but it is not recommended due to the potential for confusion and readability issues.

In summary, the maximum possible length of an identifier in Python is approximately 31 characters.


#4)What will be the value of the following Python Expression
# 4+3%5
1.3 % 5 performs the modulo operation, which gives the remainder of 3 divided by 5. The result is 3.
2.4 + 3 adds the result of the modulo operation to 4.
3.The final result is 7.
print(4+3%5)#ans7

#5) what does ~4 evaluate to?****************************************************************************************************
The bitwise NOT operator (~) in Python inverts the bits of a number. When applied to the integer 4, the binary representation of 4 is 00000100. Applying the bitwise NOT operator to 4 inverts the bits, resulting in 11111011 in binary.

To convert the binary representation back to a decimal number, you can use the int() function with the base set to 2. Here's the Python code to evaluate ~4:
result = ~4
decimal_result = int(bin(result)[2:], 2)
print(decimal_result)

Running this code will output -5, which is the decimal representation of the binary number 11111011.

So, ~4 evaluates to -5.

print(~4)

6) What is the value of the following expression?
float(22//3+3/3)
A)8
B)8.0
C)8.3
D)8.33
print(float(22//3+3/3))#ans 8.0

7)What is the type of inf?
ABoolean
BInteger
CFloat
DComplex
The type of inf in Python is a float.

In Python, inf represents positive infinity. It is a floating-point value and can be used in mathematical calculations. The type of inf is float.

print(type(inf))

#8)Which of the following is the truncation pision operator?
A/
B%
C//
D|
The truncation (or floor) division operator in Python is //.************************************************************

In the given code block, the operator // is used to perform floor division, which rounds down the result to the nearest integer. For example:
x = 10 // 3
print(x)  # Output: 3

In this case, 10 // 3 evaluates to 3 because 10 divided by 3 is 3.333..., and the // operator truncates the decimal part to 0.

So, the correct answer is:
C//

9)What is the value of the following expression?
8/4/2, 8/(4/2)
A(1.0, 4.0)
B(1.0, 1.0)
C(4.0. 1.0)
D(4.0, 4.0)
The value of the expression 8/4/2 is 1.0.
The value of the expression 8/(4/2) is 4.0.
So, the correct answer is:
B(1.0, 4.0)
"""
x = int(43.55+2/2)







# x=4+3%5
# print(x)
