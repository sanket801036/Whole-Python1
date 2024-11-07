
1. **What are strings in Python?**
   - In Python, strings are sequences of characters enclosed in quotes (single, double, or triple). Strings are immutable, meaning they cannot be changed once created.

2. **How do you reverse a string in Python?**
   - You can reverse a string by slicing it:
     ```python
     string = "hello"
     reversed_string = string[::-1]
     # Output: "olleh"
     ```

3. **How can you check if a string is a palindrome?**
   - A palindrome reads the same forwards and backwards. You can compare the string to its reverse:
     ```python
     def is_palindrome(s):
         return s == s[::-1]
     # Example: is_palindrome("madam") returns True
     ```

4. **Explain the difference between `split()` and `join()` in Python.**
   - `split()` divides a string into a list based on a specified delimiter:
     ```python
     text = "apple,banana,orange"
     result = text.split(",")  # Output: ['apple', 'banana', 'orange']
     ```
   - `join()` combines a list of strings into a single string, using a specified separator:
     ```python
     fruits = ['apple', 'banana', 'orange']
     result = ", ".join(fruits)  # Output: "apple, banana, orange"
     ```

5. **How do you find all occurrences of a substring in a string?***********************************************
   - You can use the `find()` method in a loop or regular expressions to find multiple occurrences:
     ```python
     text = "hello world, hello universe"
     occurrences = [i for i in range(len(text)) if text.startswith("hello", i)]
     # Output: [0, 13]
     ```

6. **How do you remove leading and trailing whitespaces from a string?**
   - Use the `strip()` method:
     ```python
     text = "   hello   "
     stripped_text = text.strip()  # Output: "hello"
     ```

7. **How can you count the occurrences of each character in a string?**
   - You can use the `Counter` class from the `collections` module:
     ```python
     from collections import Counter
     text = "hello"
     count = Counter(text)
     # Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})
     ```

8. **What is string interpolation, and how can you use it in Python?**
   - String interpolation is inserting values into a string. Python provides multiple ways:
     ```python
     name = "Alice"
     age = 30
     # Using f-strings
     greeting = f"My name is {name} and I am {age} years old."
     ```

9. **How do you replace a substring within a string?**
   - Use the `replace()` method:
     ```python
     text = "Hello world"
     new_text = text.replace("world", "Python")  # Output: "Hello Python"
     ```

10. **How can you check if a string contains only digits?**
    - Use the `isdigit()` method:
      ```python
      text = "12345"
      is_digit = text.isdigit()  # Output: True
      ```

11. **What are raw strings in Python?**
    - Raw strings (prefixed with `r`) treat backslashes as literal characters, which is useful for regular expressions:
      ```python
      raw_string = r"C:\Users\name"  # No need to escape backslashes
      ```

12. **How can you capitalize each word in a string?*************************************************
    - Use the `title()` method:
      ```python
      text = "hello world"
      capitalized_text = text.title()  # Output: "Hello World"
      ```

13. **How do you format strings in Python using the `.format()` method?**
    - You can insert values into placeholders marked by `{}`:
      ```python
      text = "My name is {} and I am {} years old.".format("Alice", 30)
      print(text)      
```

14. **Explain `startswith()` and `endswith()` methods.**
    - These methods check if a string starts or ends with a particular substring:
      ```python
      text = "hello world"
      starts_with_hello = text.startswith("hello")  # True
      ends_with_world = text.endswith("world")  # True
      ```

15. **How can you find the length of a string?**
    - Use the `len()` function:
      ```python
      text = "hello"
      length = len(text)  # Output: 5
      ```

16. **How do you convert a string to lowercase or uppercase?**
    - Use `lower()` for lowercase and `upper()` for uppercase:
      ```python
      text = "Hello"
      lower_text = text.lower()  # Output: "hello"
      upper_text = text.upper()  # Output: "HELLO"
      ```

These questions cover fundamental string operations and are commonly asked in Python interviews.