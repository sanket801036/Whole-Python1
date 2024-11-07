# String formatting in Python is a powerful feature for creating and manipulating strings. Here are 20 practical interview questions and answers on string formatting:

# ### 1. **What are the different ways to format strings in Python?**
# - Python supports several methods: `%` formatting, `str.format()`, and f-strings.
# % formatting
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
str.format()
print("Name: {}, Age: {}".format(name, age))

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")


# ### 2. **How do you format a number with commas as thousands separators?**
# - **Explanation:** Use `str.format()` or f-strings with formatting options.
number = 1234567
#     print("{:,}".format(number))  # Output: 1,234,567
#     print(f"{number:,}")          # Output: 1,234,567


# ### 3. **How can you specify the width of a field in string formatting?**
# - **Explanation:** Use width specifiers to align text.
#     text = "Hello"
#     print("{:<10}".format(text))  # Left align within 10 characters
#     print("{:>10}".format(text))  # Right align within 10 characters
#     print("{:^10}".format(text))  # Center align within 10 characters
#     ```

# ### 4. **How do you format floating-point numbers to a specific number of decimal places?**
# - **Explanation:** Use precision specifiers.
#     number = 3.14159
#     print("{:.2f}".format(number))  # Output: 3.14
#     print(f"{number:.2f}")          # Output: 3.14

# ### 5. **How do you include a literal brace `{}` in a formatted string using `str.format()`?**
# - **Explanation:** Double the braces to escape them.
#     print("{{}}")          # Output: {}
#     print("{{0}}".format(1))  # Output: {0}

# ### 6. **How can you format a string to ensure it’s left-padded with zeros?**
# - **Explanation:** Use zero padding with format specifiers.
#     number = 42
#     print("{:05}".format(number))  # Output: 00042
#     print(f"{number:05}")          # Output: 00042

# ### 7. **How do you format a date using `str.format()`?**
# - **Explanation:** Use `strftime` format codes.
#     from datetime import datetime
#     now = datetime.now()
#     print("{:%Y-%m-%d %H:%M:%S}".format(now))  # Output: current date and time
#     print(f"{now:%Y-%m-%d %H:%M:%S}")         # Output: current date and time

# ### 8. **How can you format a string to show a percentage?**
# - **Explanation:** Use the percentage format specifier.
#     value = 0.1234
#     print("{:.2%}".format(value))  # Output: 12.34%
#     print(f"{value:.2%}")         # Output: 12.34%

# ### 9. **How do you format a string to align text within a certain width using f-strings?**
# - **Explanation:** Use alignment specifiers.
#     text = "Align"
#     print(f"{text:<10}")  # Left align within 10 characters
#     print(f"{text:>10}")  # Right align within 10 characters
#     print(f"{text:^10}")  # Center align within 10 characters

# ### 10. **How can you use `str.format()` to insert a dictionary value into a string?**
# - **Explanation:** Use dictionary unpacking.
data = {'name': 'Alice', 'age': 30}
print("Name: {name}, Age: {age}".format(**data)) 
# Output: Name: Alice, Age: 30

# ### 11. **How do you use f-strings to format numbers with thousands separators?**
# - **Explanation:** Use the comma `,` format specifier.
number = 987654321
print(f"{number:,}")  
# Output: 987,654,321

# ### 12. **How can you format a string to include an object’s attributes?**
# - **Explanation:** Use object attributes within f-strings or `str.format()`.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Bob", 25)
print(f"Name: {person.name}, Age: {person.age}")
# Output: Name: Bob, Age: 25

# ### 13. **How do you format a number as hexadecimal using `str.format()`?**
# - **Explanation:** Use the `x` format specifier.
number = 255
print("{:x}".format(number))  # Output: ff
print(f"{number:x}")         # Output: ff

# ### 14. **How can you format a string to display scientific notation?**
# - **Explanation:** Use the `e` format specifier.
number = 12345.6789
print("{:.2e}".format(number))  # Output: 1.23e+04
print(f"{number:.2e}")         # Output: 1.23e+04


# ### 15. **How do you format strings with leading or trailing whitespace?**
# - **Explanation:** Use width and alignment specifiers.
text = "Hello"
# Right align within 10 characters (default is right alignment)
print(f"{text:>10}")
# Left align within 10 characters
print(f"{text:<10}")
# Center align within 10 characters
print(f"{text:^10}")
# output:-
#      Hello
# Hello
#   Hello

# ### 16. **How can you format a string to show a negative number in parentheses?**
# - **Explanation:** Use custom formatting.
number = -1234.56
# Check if the number is negative and format accordingly
formatted_number = f"({abs(number):,.2f})" if number < 0 else f"{number:,.2f}"
print(formatted_number)
# (1,234.56)

# Explanation:
# abs(number): This returns the absolute value of number, which removes the negative sign.
# number < 0: This checks if the number is negative.
# {abs(number):,.2f}: This formats the absolute value of the number with commas as thousand separators and two decimal places.
# ({abs(number):,.2f}): This adds parentheses around the formatted number if it is negative.
# {number:,.2f}: This formats the number with commas as thousand separators and two decimal places if the number is positive.
# This code ensures that negative numbers are shown in parentheses, while positive numbers are displayed normally.

# Example output for a negative number
# Output: (1,234.56)

# ### 17. **How do you format a string to include the current time and date in ISO format?**
# -Use `strftime` format codes with `datetime`.
from datetime import datetime
now = datetime.now()
print(f"{now.isoformat()}")  # Output: current date and time in ISO format
#2024-07-30T10:44:39.465689

# ### 18. **How can you use `str.format()` to format a list of numbers into a comma-separated string?**
# - **Explanation:** Use `str.join()` with list comprehension.
numbers = [1, 2, 3, 4, 5]
f = ', '.join("{:d}".format(num) for num in numbers)
print(f) 
# Output: 1, 2, 3, 4, 5

# ### 19. **How do you format a string to include a URL with specific query parameters?**
# - Use `str.format()` or f-strings to include query parameters.
base_url = "http://example.com"
endpoint = "search"
query = "python"
url = f"{base_url}/{endpoint}?q={query}"
print(url)  
# Output: http://example.com/search?q=python

# ### 20. **How can you format a string to include a variable number of arguments using `str.format()`?**
# - **Explanation:** Use `*args` to handle a variable number of arguments.
def format_string(*args):
    return " ".join(map(str, args))
formatted = format_string("Hello", "world", 123)
print(formatted) 
 # Output: Hello world 123

# These questions cover various practical aspects of string formatting in Python, including different formatting methods, handling numbers, dates, and custom formats.