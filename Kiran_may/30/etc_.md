Here are 20 tricky and logical Python interview questions related to area, perimeter, volume, simple interest, total price, tax, total interest, compound interest, speed, average, and total amount after a discount, along with their answers:

### 1. **Calculate the Area of a Circle**
```python
import math
def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(5))  # Example for radius 5
```

### 2. **Calculate the Perimeter of a Rectangle**
```python
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

print(perimeter_of_rectangle(5, 3))  # Example for length 5 and width 3
```

### 3. **Calculate the Volume of a Cylinder**
```python
import math
def volume_of_cylinder(radius, height):
    return math.pi * radius ** 2 * height

print(volume_of_cylinder(3, 5))  # Example for radius 3 and height 5
```

### 4. **Simple Interest Calculation**
```python
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(1000, 5, 3))  # Example: P=1000, R=5%, T=3 years
```

### 5. **Total Price Including Tax**
```python
def total_price(price, tax_rate):
    return price + (price * tax_rate / 100)

print(total_price(500, 10))  # Example: Price=500, Tax Rate=10%
```

### 6. **Total Interest on a Loan**
```python
def total_interest(principal, rate, time):
    return principal * rate * time / 100

print(total_interest(2000, 7, 2))  # Example: P=2000, R=7%, T=2 years
```

### 7. **Compound Interest Calculation**
```python
def compound_interest(principal, rate, time, times_compounded):
    return principal * (1 + rate / (100 * times_compounded))**(times_compounded * time) - principal

print(compound_interest(1000, 5, 2, 4))  # P=1000, R=5%, T=2 years, compounded quarterly
```

### 8. **Calculate Speed**
```python
def speed(distance, time):
    return distance / time

print(speed(100, 2))  # Example: Distance=100 km, Time=2 hours
```

### 9. **Calculate Average of a List of Numbers**
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print(calculate_average([10, 20, 30, 40]))  # Example list of numbers
```

### 10. **Total Amount After a Discount**
```python
def total_after_discount(price, discount):
    return price - (price * discount / 100)

print(total_after_discount(500, 20))  # Example: Price=500, Discount=20%
```

### 11. **Calculate Area of a Triangle**
```python
def area_of_triangle(base, height):
    return 0.5 * base * height

print(area_of_triangle(10, 5))  # Example: Base=10, Height=5
```

### 12. **Calculate Perimeter of a Square**
```python
def perimeter_of_square(side):
    return 4 * side

print(perimeter_of_square(6))  # Example: Side=6
```

### 13. **Calculate Volume of a Sphere**
```python
import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3

print(volume_of_sphere(7))  # Example: Radius=7
```

### 14. **Calculate Compound Interest with Monthly Compounding**
```python
def compound_interest_monthly(principal, rate, time):
    times_compounded = 12
    return principal * (1 + rate / (100 * times_compounded))**(times_compounded * time) - principal

print(compound_interest_monthly(1000, 5, 2))  # P=1000, R=5%, T=2 years, compounded monthly
```

### 15. **Total Amount with Multiple Discounts**
```python
def total_after_multiple_discounts(price, discounts):
    for discount in discounts:
        price -= price * discount / 100
    return price

print(total_after_multiple_discounts(1000, [10, 20]))  # Example: 10% followed by 20%
```

### 16. **Calculate Total Price After Adding Service Tax**
```python
def total_price_with_service_tax(price, service_tax_rate):
    return price + (price * service_tax_rate / 100)

print(total_price_with_service_tax(1000, 12))  # Price=1000, Service Tax=12%
```

### 17. **Find Time Given Distance and Speed**
```python
def time(distance, speed):
    return distance / speed

print(time(100, 50))  # Example: Distance=100 km, Speed=50 km/h
```

### 18. **Calculate Total Price After Sales Tax and Discount**
```python
def total_price_tax_discount(price, tax_rate, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price + (discounted_price * tax_rate / 100)

print(total_price_tax_discount(1000, 18, 10))  # Price=1000, Tax=18%, Discount=10%
```

### 19. **Calculate Total Interest with Different Interest Rates**
```python
def total_interest_different_rates(principal, rate1, rate2, time1, time2):
    interest1 = principal * rate1 * time1 / 100
    interest2 = principal * rate2 * time2 / 100
    return interest1 + interest2

print(total_interest_different_rates(1000, 5, 7, 2, 3))  # Example
```

### 20. **Calculate the Perimeter of a Triangle Given 3 Sides**
```python
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

print(perimeter_of_triangle(3, 4, 5))  # Example
```

These examples cover a wide range of calculations that may involve complex combinations of operations and logical conditions, suitable for technical interviews.