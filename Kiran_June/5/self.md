### 1. What are the different types of operators in Python?
- **Explanation:** Python supports various types of operators including arithmetic, relational, logical, bitwise, assignment, membership, and identity operators.

### 2. How do arithmetic operators work in Python? Provide examples.
- **Explanation:** Arithmetic operators perform basic mathematical operations.

    a = 10
    b = 3
    print(a + b)  # Addition: 13
    print(a - b)  # Subtraction: 7
    print(a * b)  # Multiplication: 30
    print(a / b)  # Division: 3.333...
    print(a % b)  # Modulus: 1
    print(a ** b) # Exponentiation: 1000
    print(a // b) # Floor Division: 3

0 ## 3. How do comparison (relational) operators work in Python? Provide examples.
- **Explanation:** Comparison operators compare two values and return a Boolean result.

    a = 5
    b = 10
    print(a == b)  # Equal: False
    print(a != b)  # Not Equal: True
    print(a > b)   # Greater than: False
    print(a < b)   # Less than: True
    print(a >= b)  # Greater than or equal to: False
    print(a <= b)  # Less than or equal to: True

### 4. How do logical operators work in Python? Provide examples.
- **Explanation:** Logical operators are used to combine conditional statements.
    a = True
    b = False
    print(a and b) # Logical AND: False
    print(a or b)  # Logical OR: True
    print(not a)   # Logical NOT: False

### 5. How do bitwise operators work in Python? Provide examples.
- **Explanation:** Bitwise operators perform operations on binary representations of integers.

    a = 6  # 110 in binary
    b = 3  # 011 in binary
    print(a & b)  # Bitwise AND: 2 (010 in binary)
    print(a | b)  # Bitwise OR: 7 (111 in binary)
    print(a ^ b)  # Bitwise XOR: 5 (101 in binary)
    print(~a)     # Bitwise NOT: -7 (inverts all bits)
    print(a << 1) # Bitwise left shift: 12 (1100 in binary)
    print(a >> 1) # Bitwise right shift: 3 (011 in binary)

### 6. How do assignment operators work in Python? Provide examples.
- **Explanation:** Assignment operators are used to assign values to variables.
    a = 5
    a += 2  # Equivalent to a = a + 2
    print(a) # Output: 7
    a -= 1  # Equivalent to a = a - 1
    print(a) # Output: 6
    a *= 3  # Equivalent to a = a * 3
    print(a) # Output: 18
    a /= 2  # Equivalent to a = a / 2
    print(a) # Output: 9.0
    a %= 4  # Equivalent to a = a % 4
    print(a) # Output: 1.0
    a **= 3 # Equivalent to a = a ** 3
    print(a) # Output: 1.0
    a //= 2 # Equivalent to a = a // 2
    print(a) # Output: 0.0

### 7. What is the difference between `is` and `==` in Python?
- **Explanation:** `is` checks for object identity, whereas `==` checks for value equality.************************************************************************************************************
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(a == c)  # True, because values are equal
    print(a is c)  # False, because they are different objects
    print(a is b)  # True, because they are the same object
    ```

### 8. How do membership operators work in Python? Provide examples.
- **Explanation:** Membership operators test for membership in a sequence (e.g., strings, lists).

    a = [1, 2, 3, 4, 5]
    print(3 in a)    # True
    print(6 not in a) # True

### 9. How do identity operators work in Python? Provide examples.
- **Explanation:** Identity operators compare the memory locations of two objects.
    a = 10
    b = 10
    c = a
    print(a is b)  # True
    print(a is c)  # True
    b = 11
    print(a is b)  # False

## 10. How can you use operators with lists in Python? Provide examples.
- **Explanation:** You can use arithmetic and membership operators with lists.
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)    # Concatenation: [1, 2, 3, 4, 5, 6]
    print(a * 2)    # Repetition: [1, 2, 3, 1, 2, 3]
    print(3 in a)   # Membership: True
    print(4 not in a) # Membership: True

### 11. How do augmented assignment operators work with lists and strings?
- **Explanation:** Augmented assignment operators modify the variable in place if possible.
    a = [1, 2, 3]
    a += [4, 5]
    print(a) # Output: [1, 2, 3, 4, 5]
    
    s = "Hello"
    s += " World"
    print(s) # Output: "Hello World"


### 12. How do you use the ternary operator in Python? Provide an example.
- **Explanation:** The ternary operator in Python is used for conditional expressions.
    a = 10
    b = 20
    result = "a is greater" if a > b else "b is greater"
    print(result) # Output: "b is greater"

### 13. How do the `and` and `or` operators work with non-Boolean values in Python?
- **Explanation:** `and` returns the first falsey value or the last value, `or` returns the first truthy value or the last value.
    print(0 and 1)  # Output: 0
    print(1 and 0)  # Output: 0
    print(1 and 2)  # Output: 2
    print(0 or 1)   # Output: 1
    print(1 or 0)   # Output: 1
    print(0 or 2)   # Output: 2
    ```

### 14. How do you use bitwise operators to set, clear, and toggle specific bits in an integer?
- **Explanation:** Use bitwise operators to manipulate specific bits.

    a = 0b1010  # 10 in decimal
    # Set the 1st bit
    a |= 0b0100  # 14 in decimal
    print(bin(a))
    # Clear the 2nd bit
    a &= ~0b0010  # 12 in decimal
    print(bin(a))
    # Toggle the 3rd bit
    a ^= 0b1000  # 4 in decimal
    print(bin(a))

### 15. How can you use the `in` operator with dictionaries?
- **Explanation:** The `in` operator checks if a key exists in a dictionary.

    my_dict = {'a': 1, 'b': 2}
    print('a' in my_dict)    # Output: True
    print('c' in my_dict)    # Output: False

 ## 16. How do you use the `**` operator with function arguments?
- **Explanation:** The `**` operator unpacks a dictionary into keyword arguments.

    def my_function(a, b, c):
        print(a, b, c)

    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_function(**my_dict)  # Output: 1 2 3

 ## 17. Explain how operator overloading works in Python with an example.
- **Explanation:** Operator overloading allows you to define custom behavior for operators in user-defined classes.

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1 + p2)  # Output: Point(4, 6)

### 18. How do you use the `is not` operator in Python? Provide an example.
- **Explanation:** `is not` checks if two variables refer to different objects.

    ```python
    a = 10
    b = 20
    print(a is not b)  # Output: True

### 19. How can you use the `@` operator in Python?
- **Explanation:** The `@` operator is used for matrix multiplication.

    import numpy as np
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print(a @ b)  # Matrix multiplication

### 20. What is the difference between `//` and `/` operators in Python?
- **Explanation:** `/` performs floating-point division, while `//` performs floor division.
    print(10 / 3)   # Output: 3.333...
    print(10 // 3)  # Output: 3

