
### 1. **Find the Sum of Digits of a Number**
   * **Question:** Given a number, find the sum of its digits.
   * **Example:** Input: `1234`, Output: `10`

   ```python
   def sum_of_digits(n):
       return sum(int(digit) for digit in str(n))

   # Example usage
   print(sum_of_digits(1234))  # Output: 10
   ```

---



### 3. **Find the Largest Element in an Array**
   * **Question:** Given an array of integers, find the largest element.
   * **Example:** Input: `[1, 3, 5, 7, 9]`, Output: `9`

   ```python
   def find_largest(arr):
       return max(arr)

   # Example usage
   print(find_largest([1, 3, 5, 7, 9]))  # Output: 9
   ```

### 5. **Calculate Simple Interest**
   * **Question:** Given principal (`P`), rate of interest (`R`), and time (`T`), calculate simple interest.
   * **Formula:** `Simple Interest = (P * R * T) / 100`
   * **Example:** Input: `P = 1000, R = 5, T = 2`, Output: `100`

   ```python
   def calculate_simple_interest(P, R, T):
       return (P * R * T) / 100

   # Example usage
   print(calculate_simple_interest(1000, 5, 2))  # Output: 100
   ```


### 7. **Fibonacci Sequence up to N Terms**
   * **Question:** Print the Fibonacci sequence up to `n` terms.
   * **Example:** Input: `5`, Output: `[0, 1, 1, 2, 3]`

   ```python
   def fibonacci(n):
       sequence = [0, 1]
       while len(sequence) < n:
           sequence.append(sequence[-1] + sequence[-2])
       return sequence[:n]

   # Example usage
   print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
   ```

---

### 8. **Calculate Compound Interest**
   * **Question:** Given principal (`P`), rate of interest (`R`), and time (`T`), calculate compound interest.
   * **Formula:** `Compound Interest = P * (1 + R/100)^T - P`
   * **Example:** Input: `P = 1000, R = 5, T = 2`, Output: `102.5`

   ```python
   def calculate_compound_interest(P, R, T):
       return P * ((1 + R / 100) ** T) - P

   # Example usage
   print(calculate_compound_interest(1000, 5, 2))  # Output: 102.5
   ```


### 10. **Find the GCD of Two Numbers**
   * **Question:** Write a function to find the greatest common divisor (GCD) of two numbers.
   * **Example:** Input: `54, 24`, Output: `6`

   ```python
   import math

   def find_gcd(a, b):
       return math.gcd(a, b)

   # Example usage
   print(find_gcd(54, 24))  # Output: 6
   ```
