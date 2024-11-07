### 1. Check if a Number is Prime
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(15))

### 2. Check if a Number is Perfect
# A perfect number is a number that is equal to the sum of its proper divisors (excluding the number itself).
def is_perfect(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

print(is_perfect(15))

### 3. Check if a Word is a Palindrome
# A palindrome is a word that reads the same forwards and backwards.
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('madam'))


### 4. Check if a Number is an Armstrong Number
# An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its digits raised to the power of the number of digits.
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return n == sum(d**num_digits for d in digits)
print(is_armstrong(17))

### 5. Print a Pattern

def pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)
print(pattern(5))


# *
# **
# ***
# ****
# *****