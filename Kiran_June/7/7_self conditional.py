# Certainly! Here are 20 simple practice coding questions focused on conditional statements in Python:

# 1. **Check if a number is positive, negative, or zero.**

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
check_number(50)

# 2. **Determine if a number is even or odd.**
def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
 

# 3. **Find the largest of three numbers.**
#    ```python
#    def largest_of_three(a, b, c):
#        if a >= b and a >= c:
#            return a
#        elif b >= a and b >= c:
#            return b
#        else:
#            return c
#    ```

# 4. **Check if a year is a leap year.**
#    ```python
#    def is_leap_year(year):
#        if year % 4 == 0:
#            if year % 100 == 0:
#                if year % 400 == 0:
#                    return True
#                else:
#                    return False
#            else:
#                return True
#        else:
#            return False
#    ```

# 5. **Grade based on marks.**
#    ```python
#    def grade(marks):
#        if marks >= 90:
#            return 'A'
#        elif marks >= 80:
#            return 'B'
#        elif marks >= 70:
#            return 'C'
#        elif marks >= 60:
#            return 'D'
#        else:
#            return 'F'
#    ```

# 6. **Check if a character is a vowel or consonant.**
#    ```python
#    def is_vowel_or_consonant(char):
#        vowels = "aeiouAEIOU"
#        if char in vowels:
#            return "Vowel"
#        else:
#            return "Consonant"
#    ```

# 7. **Check if a number is divisible by both 3 and 5.**
#    def is_divisible_by_3_and_5(n):
#        if n % 3 == 0 and n % 5 == 0:
#            return True
#        else:
#            return False

# 8. **Find the smallest of four numbers.**
#    def smallest_of_four(a, b, c, d):
#        if a <= b and a <= c and a <= d:
#            return a
#        elif b <= a and b <= c and b <= d:
#            return b
#        elif c <= a and c <= b and c <= d:
#            return c
#        else:
#            return d

# 9. **Check if a number is a multiple of 10.**
#    def is_multiple_of_10(n):
#        if n % 10 == 0:
#            return True
#        else:
#            return False


# 10. **Determine if a string is a palindrome.**
#     def is_palindrome(s):
#         if s == s[::-1]:
#             return True
#         else:
#             return False

# 11. **Check if a number is within a range (inclusive).**
#     def is_within_range(n, start, end):
#         if start <= n <= end:
#             return True
#         else:
#             return False

# 12. **Check if a person is eligible to vote (age >= 18).**

#     def can_vote(age):
#         if age >= 18:
#             return True
#         else:
#             return False

# 13. **Check if a number is prime.**
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True

# 14. **Classify a number as small, medium, or large (1-10: small, 11-100: medium, >100: large).**
#     def classify_number(n):
#         if 1 <= n <= 10:
#             return "Small"
#         elif 11 <= n <= 100:
#             return "Medium"
#         else:
#             return "Large"

# 15. **Determine the season based on the month number (1-12).**
#     def determine_season(month):
#         if month in [12, 1, 2]:
#             return "Winter"
#         elif month in [3, 4, 5]:
#             return "Spring"
#         elif month in [6, 7, 8]:
#             return "Summer"
#         elif month in [9, 10, 11]:
#             return "Autumn"
#         else:
#             return "Invalid month"

# 16. **Check if a number is a perfect square.**
#     def is_perfect_square(n):
#         if int(n**0.5)**2 == n:****************************************************************************
#             return True
#         else:
#             return False

# 17. **Determine if a string starts with a vowel.**
#     def starts_with_vowel(s):
#         if s[0].lower() in "aeiou":
#             return True
#         else:
#             return False

# 18. Check if a number is positive and even.
#     def is_positive_and_even(n):
#         if n > 0 and n % 2 == 0:
#             return True
#         else:
#             return False

# 19.Check if a number is within a specific range and divisible by a given number.
#     def is_within_range_and_divisible(n, start, end, divisor):
#         if start <= n <= end and n % divisor == 0:
#             return True
#         else:
#             return False

# 20. **Check if a string contains only uppercase letters.**
#     def is_all_uppercase(s):
#         if s.isupper():
#             return True
#         else:
#             return False

# These practice questions cover a range of basic scenarios to help you solidify your understanding and application of conditional statements in Python.
