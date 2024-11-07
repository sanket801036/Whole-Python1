# Here are 30 practical interview questions related to conditional statements in Python, along with brief explanations for each:

# ### 1. What are the basic conditional statements in Python?
# - **Explanation:** The basic conditional statements are `if`, `elif`, and `else`.
#     if condition:
#         # code
#     elif another_condition:
#         # code
#     else:
#         # code

# ### 2. How do you use `if` statements in Python? Provide an example.
# - **Explanation:** An `if` statement executes a block of code if its condition is true.
#     a = 10
#     if a > 5:
#         print("a is greater than 5")

# ### 3. What is the purpose of `elif` in Python?
# - **Explanation:** `elif` allows you to check multiple conditions in sequence after the initial `if` condition.

#     a = 10
#     if a > 10:
#         print("a is greater than 10")
#     elif a == 10:
#         print("a is equal to 10")
#     else:
#         print("a is less than 10")


# ### 4. How does the `else` statement work in Python?
# - **Explanation:** The `else` block executes if all preceding `if` and `elif` conditions are false.
#     a = 5
#     if a > 5:
#         print("a is greater than 5")
#     else:
#         print("a is not greater than 5")

# ### 5. Can you nest `if` statements in Python? Provide an example.
# - **Explanation:** Yes, `if` statements can be nested within each other.

#     a = 10
#     if a > 5:
#         if a < 15:
#             print("a is between 5 and 15")
# ### 6. How do you use logical operators (`and`, `or`, `not`) in conditional statements?
# - **Explanation:** Logical operators combine multiple conditions.

#     a = 5
#     b = 10
#     if a < 10 and b > 5:
#         print("Both conditions are true")
#     if a < 10 or b < 5:
#         print("At least one condition is true")
#     if not (a > 10):
#         print("a is not greater than 10")

# ### 7. How do you use conditional expressions (ternary operator) in Python?
# - **Explanation:** The ternary operator allows you to assign values based on a condition.
#     a = 10
#     result = "Even" if a % 2 == 0 else "Odd"
#     print(result)

# ### 8. How can you check if a value is in a list using a conditional statement?
# - **Explanation:** Use the `in` keyword.
#     a = 5
#     my_list = [1, 2, 3, 4, 5]
#     if a in my_list:
#         print("a is in the list")

# ### 9. How do you use `is` and `is not` in conditional statements?
# - **Explanation:** `is` checks if two variables refer to the same object, while `is not` checks if they do not.
#     a = [1, 2, 3]
#     b = a
#     if a is b:
#         print("a and b refer to the same object")
#     if a is not [1, 2, 3]:
#         print("a and [1, 2, 3] are not the same object")

# ### 10. How do you use conditional statements to validate user input?
# - **Explanation:** You can use conditional statements to check if the user input meets certain criteria.
#     user_input = input("Enter a number: ")
#     if user_input.isdigit():
#         print("Valid number")
#     else:
#         print("Invalid input")

# ### 11. How can you use `if` statements to implement a basic switch-case behavior in Python?
# - **Explanation:** Use `if-elif-else` statements to mimic a switch-case construct.

#     case = 2
#     if case == 1:
#         print("Option 1")
#     elif case == 2:
#         print("Option 2")
#     elif case == 3:
#         print("Option 3")
#     else:
#         print("Default option")


# ### 12. How do you handle multiple conditions using nested `if` statements?
# - **Explanation:** Nest `if` statements to handle more complex logic.
#     a = 10
#     b = 20
#     if a > 5:
#         if b > 15:
#             print("Both conditions are true")

# ### 13. What is short-circuit evaluation in conditional statements?
# - **Explanation:** Short-circuit evaluation means Python will stop evaluating as soon as the result is determined.

#     def func1():
#         print("func1 called")
#         return True

#     def func2():
#         print("func2 called")
#         return False

#     if func1() or func2():
#         print("Condition met")


# ### 14. How can you use `try-except` blocks in conjunction with conditional statements?
# - **Explanation:** Use `try-except` blocks to handle exceptions that might occur in conditional statements.

# try:
#     a = int(input("Enter a number: "))
#     if a > 10:
#         print("Number is greater than 10")
# except ValueError:
#     print("Invalid input")

# ### 15. How do you use `if` statements to check for empty values or collections?
# - **Explanation:** Use `if not` to check if a collection or value is empty.
#     my_list = []
#     if not my_list:
#         print("The list is empty")


# ### 16. How can you compare strings using conditional statements?
# - **Explanation:** Use comparison operators to compare strings lexicographically.

#     str1 = "apple"
#     str2 = "banana"
#     if str1 < str2:
#         print("str1 comes before str2")



# ### 17. How do you use conditional statements to implement a basic authentication system?
# - **Explanation:** Check user credentials using `if` statements.
#     username = "admin"
#     password = "password123"
#     user_input = input("Enter username: ")
#     pass_input = input("Enter password: ")

#     if user_input == username and pass_input == password:
#         print("Authenticated")
#     else:
#         print("Authentication failed")

# ### 18. How do you use conditional statements to validate the format of an email address?
# - **Explanation:** Use `if` statements along with string methods to check the format.

email = "example@example.com"
if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")

# ### 19. How can you use conditional statements to check if a number is prime?
# - **Explanation:** Implement a function that uses `if` statements to check for prime numbers.
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     print(is_prime(11))  # Output: True

# ### 20. How do you use conditional statements to determine the grade based on a score?
# - **Explanation:** Use `if-eif-else` to map scores to grades.
#     score = 85
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     print(f"Grade: {grade}")

# ### 21. How can you use conditional statements to handle different file extensions?
# - **Explanation:** Check the file extension using `if-elif-else`.

    #  file_name = "document.pdf"
#     if file_name.endswith(".txt"):
#         print("Text file")
#     elif file_name.endswith(".pdf"):
#         print("PDF file")
#     else:
#         print("Other file type")


# ### 22. How do you use conditional statements to implement feature toggles?
# - **Explanation:** Use `if` statements to enable or disable features based on conditions.
#     feature_enabled = True
#     if feature_enabled:
#         print("Feature is enabled")
#     else:
#         print("Feature is disabled")

# ### 23. How can you use conditional statements to determine if a number is positive, negative, or zero?
# - **Explanation:** Use `if-elif-else` to classify numbers.
#     num = -5
#     if num > 0:
#         print("Positive")
#     elif num < 0:
#         print("Negative")
#     else:
#         print("Zero")

# ### 24. How do you use conditional statements to check if a value is of a specific type?
# - **Explanation:** Use `isinstance` to check the type.
#     value = 42
#     if isinstance(value, int):
#         print("Value is an integer")

# ### 25. How can you use conditional statements to handle different types of input (e.g., number vs. string)?
# - **Explanation:** Use `if-elif-else` with type checking.
#     value = "hello"
#     if isinstance(value, str):
#         print("Value is a string")
#     elif isinstance(value, int):
#         print("Value is an integer")
#     else:
#         print("Unknown type")

# ### 26. How do you use conditional statements to filter data based on multiple criteria?
# - **Explanation:** Combine multiple conditions using logical operators.
#     age = 25
#     income = 50000
#     if age > 18 and income > 30000:
#         print("Eligible")

# ### 27. How can you use conditional statements to check if a string contains only alphabetic characters?
# - **Explanation:** Use string methods and conditional checks.
#     text = "HelloWorld"
#     if text.isalpha():
#         print("String contains only alphabetic characters")

# ### 28. How do you handle conditional statements in a loop to perform actions based on different cases?
# - **Explanation:** Use `if-elif-else` within a loop to handle different cases.
#     for i in range(5):
#         if i == 0:
#             print("Zero")
#         elif i == 1:
#             print("One")
#         else:
#             print("Other")

# ### 29. How can you use conditional statements to determine the maximum of three numbers?
# - **Explanation:** Use `if-elif-else` to find the maximum.
#     a = 10
#     b = 20
#     c = 15
#     if a >= b and a >= c:
#         print("a is the largest")
#     elif b >= a and b >= c:
#         print("b is the largest")
#     else:
#         print("c is the largest")

# ### 30. How do you use conditional statements to validate a password against multiple criteria (e.g., length, special characters)?
#**Explanation:** Use `if-elif-else` to check multiple password criteria.
#     password = "P@ssw0rd"
#     if len(password) < 8:
#         print("Password too short")
#     elif not any(char.isdigit() for char in password):
#         print("Password must contain a digit")
#     elif not any(char.isupper() for char in password):
#         print("Password must contain an uppercase letter")
#     elif not any(char in "!@#$%^&*()" for char in password):
#         print("Password must contain a special character")
#     else:
#         print("Password is valid")

# These questions cover a broad range of practical scenarios where conditional statements are used, helping to assess both basic and advanced understanding of this fundamental programming concept.
