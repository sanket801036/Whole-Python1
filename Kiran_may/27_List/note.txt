2. How do you reverse a string in Python?
s = "hello"
r = s[::-1]
# Output: "olleh"

3. How can you check if a string is a palindrome?
def p(s):
    return s == s[::-1]
# Example: p("madam") returns True

4. Explain the difference between split() and join() in Python.
 * split() divides a string into a list:
   t = "apple,banana,orange"
r = t.split(",")  # Output: ['apple', 'banana', 'orange']

 * join() combines a list of strings:
   f = ['apple', 'banana', 'orange']
r = ", ".join(f)  # Output: "apple, banana, orange"

5. How do you find all occurrences of a substring in a string?
t = "hello world, hello universe"
o = [i for i in range(len(t)) if t.startswith("hello", i)]
# Output: [0, 13]

6. How do you remove leading and trailing whitespaces from a string?
t = "   hello   "
s = t.strip()  # Output: "hello"

7. How can you count the occurrences of each character in a string?
from collections import Counter
t = "hello"
c = Counter(t)
# Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})

8. What is string interpolation, and how can you use it in Python?
n = "Alice"
a = 30
g = f"My name is {n} and I am {a} years old."

9. How do you replace a substring within a string?
t = "Hello world"
n = t.replace("world", "Python")  # Output: "Hello Python"

10. How can you check if a string contains only digits?
t = "12345"
d = t.isdigit()  # Output: True

11. What are raw strings in Python?
r = r"C:\Users\name"  # No need to escape backslashes

12. How can you capitalize each word in a string?
t = "hello world"
c = t.title()  # Output: "Hello World"

13. How do you format strings in Python using the .format() method?
t = "My name is {} and I am {} years old.".format("Alice", 30)

14. Explain startswith() and endswith() methods.
t = "hello world"
s = t.startswith("hello")  # True
e = t.endswith("world")  # True

15. How can you find the length of a string?
t = "hello"
l = len(t)  # Output: 5

16. How do you convert a string to lowercase or uppercase?
t = "Hello"
l = t.lower()  # Output: "hello"
u = t.upper()  # Output: "HELLO"

