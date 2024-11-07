# Transfer statements in Python are used to control the flow of execution within loops and functions. The primary transfer statements are `break`, `continue`, and `return`. Here are 20 practical interview questions and answers related to these statements:

# The `break` statement is used 
# to exit a loop prematurely when a certain condition is met.
for i in range(10):
    if i == 5:
        break
    print(i)

# 0
# 1
# 2
# 3
# 4
# In this example, the loop stops when `i` equals 5, so the numbers 0 to 4 are printed.

### `continue`
# The `continue` statement is used 
# to skip the rest of the code inside the loop 
# for the current iteration and jump to the next iteration of the loop.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 1
# 3
# 5
# 7
# 9

# In this example, the loop skips the even numbers and prints only the odd numbers from 0 to 9.

### `return`
# The `return` statement is used 
# to exit a function and optionally pass an expression back to the caller.
# Once a `return` statement is executed, the function stops executing.
def add(a, b):
    return a + b
    print("This will not be printed")

result = add(3, 4)
print(result)

# 7


### Summary
# - `break`: Exits a loop prematurely.(Stops the loop immediately and moves on to the next part of the code outside the loop.)
# - `continue`: Skips the rest of the code inside the loop for the current iteration.
# - `return`: Exits a function and optionally returns a value.


# ### 1. **What is the purpose of the `break` statement in Python?**
for i in range(10):
    if i == 5:
        break
    print(i)  # Outputs 0, 1, 2, 3, 4

# ### 2. **How does the `continue` statement work in Python?**
# - **Explanation:** `continue` skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Outputs 1, 3, 5, 7, 9

# ### 3. **What is the function of the `return` statement in a Python function?**
# - **Explanation:** `return` exits a function and optionally passes a value back to the caller.
def add(a, b):
    return a + b
result = add(3, 4)
print(result)  # Output: 7

# ### 4. **How can you use `break` to exit a loop based on user input?**
# - **Explanation:** Use `break` to exit a loop when a specific user input is encountered.
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break

# ### 5. **How do you use `continue` to skip certain iterations in a loop?**
# - **Explanation:** Use `continue` to skip over specific iterations based on a condition.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Outputs odd numbers from 1 to 9

# ### 6. **How can `return` be used to exit a function early?**
# - **Explanation:** Use `return` to exit a function before it reaches the end, often based on a condition.


def process_value(value):
    if value < 0:
        return "Negative value"
    # Process positive value
    return "Processed value"

print(process_value(-1))  # Output: Negative value


# ### 7. **How do `break`, `continue`, and `return` interact in nested loops?**
# - **Explanation:** `break` and `continue` only affect the nearest enclosing loop, while `return` affects the function's execution.

def nested_loop_example():
    for i in range(3):
        for j in range(3):
            if j == 1:
                break  # Breaks the inner loop
            print(i, j)
        print("Inner loop done")
    return "Done"
result = nested_loop_example()
print(result)

# In this example, when `j` equals 1, the `break` statement will exit the inner loop and move to the next iteration of the outer loop. The `return` statement will return the string "Done" after the loops have finished executing. 

# 0 0
# Inner loop done
# 1 0
# Inner loop done
# 2 0
# Inner loop done
# Done

# - The `break` statement exits the inner loop when `j` equals 1.
# - The `return` statement exits the function after both loops have completed.

# If you want to see how `continue` and `return` can be used in nested loops, here are additional examples:

### Using `continue` in nested loops:
def nested_loop_example_continue():
    for i in range(3):
        for j in range(3):
            if j == 1:
                continue  # Skips the rest of the inner loop for this iteration
            print(i, j)
        print("Inner loop done")

    return "Done"

result_continue = nested_loop_example_continue()
print(result_continue)

# 0 0
# 0 2
# Inner loop done
# 1 0
# 1 2
# Inner loop done
# 2 0
# 2 2
# Inner loop done
# Done


### Using `return` in nested loops:
def nested_loop_example_return():
    for i in range(3):
        for j in range(3):
            if j == 1:
                return "Stopped early"  # Exits the function immediately
            print(i, j)
        print("Inner loop done")

    return "Done"

result_return = nested_loop_example_return()
print(result_return)

# 0 0
# Stopped early

# In this case, the function exits completely and returns "Stopped early" when `j` equals 1.

# ### 8. **How can you use `break` to terminate a `while` loop?**
# - **Explanation:** Use `break` to exit a `while` loop based on a condition.
count = 0
while True:
    count += 1
    if count > 5:
        break
print(count)  # Outputs numbers from 1 to 5

# ### 9. **How does `continue` work in a `while` loop?**
# - **Explanation:** `continue` skips the rest of the loop body and starts the next iteration.
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # Outputs odd numbers from 1 to 9

# ### 10. **How can you use `return` to return multiple values from a function?**
# - **Explanation:** Use `return` to return a tuple of values.

def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total, count

total, count = get_stats([1, 2, 3, 4])
print(total, count)  # Output: 10 4

# ### 11. **How can `break` be used in a loop with `else` clause?**
# In simple words, a clause in Python refers to a part of a statement that controls the flow of the program. Clauses are usually associated with control structures like loops, conditionals, and exception handling.

### Examples of Clauses:

# 1. **`if` Clause:**
#    Controls the flow based on a condition.
   
# if x > 0:
#     print("Positive")
   
# 2. **`elif` and `else` Clauses:**
#    Used with `if` for additional conditions and a fallback case.

#    if x > 0:
#        print("Positive")
#    elif x == 0:
#        print("Zero")
#    else:
#        print("Negative")


# 3. **`for` and `while` Clauses:**
#    Used to create loops.

#    for i in range(5):
#        print(i)

#    ```python
#    while x < 10:
#        print(x)
#        x += 1
#    ```

# 4. **`try` and `except` Clauses:**
#    Used for exception handling.
#    ```python
#    try:
#        result = 10 / 0
#    except ZeroDivisionError:
#        print("Cannot divide by zero")
#    ```

# In each case, the clause defines a specific behavior or action based on certain conditions or situations.
# - **Explanation:** If `break` is executed, the `else` block will not run.
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed")

# ### 12. **How does `continue` affect the `else` clause of a loop?**
#  `continue` will skip the rest of the loop body but does not affect the `else` clause.
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Loop completed")  # This will be printed

# ### 13. **How can `return` be used to exit from nested functions?**
# - **Explanation:** `return` will exit only from the current function, not from all nested functions.
def outer():
    def inner():
        return "Returned from inner"
    return inner()
print(outer())

### Explanation:
# - `outer_function` contains another function, `inner_function`, defined within it.
# - `inner_function` returns the string "Returned from inner".
# - `outer_function` calls `inner_function` and returns its result.
# - The `print` statement calls `outer_function`, which in turn calls `inner_function`, and prints the result.

# Output: Returned from inner

### 14. How can you use `break` to manage infinite loops?
# - Explanation: `break` can be used to exit an infinite `while` loop based on a condition.
while True:
    user_input = input("Type 'stop' to exit: ")
    if user_input == 'stop':
        break
    print("You typed:", user_input)

# Output
# Type 'stop' to exit: hello
# You typed: hello
# Type 'stop' to exit: stop

# (Note: The loop will keep asking for input until 'stop' is entered, after which it will break out of the loop.)

### 15. How can `continue` be used to skip even numbers in a `for` loop?
# - Explanation: Use `continue` to skip over even numbers.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  
# Output:
# 1
# 3
# 5
# 7
# 9

### 16. How do you use `return` in a recursive function to manage recursion?
# - Explanation: `return` can be used to end a recursive function call.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Output:
# 120

### 17. How can you use `break` to exit a loop based on a condition from a list of items?
# - Explanation: Use `break` to exit the loop when a specific item is found.
items = ['apple', 'banana', 'cherry']
for item in items:
    if item == 'banana':
        break
    print(item)  # Outputs 'apple'
# Output:
# apple

# Summary:
# The loop iterates through the items list.
# When it encounters the item 'banana', it executes the break statement, which exits the loop.
# Only the item 'apple' is printed, as the loop terminates before reaching 'cherry'.
# Output:

# apple
# The break statement is useful for exiting a loop when a certain condition is met, as shown in this example where it exits the loop upon finding the item 'banana'.

### 18. How does `continue` handle exceptions in a loop?
# - Explanation: `continue` does not handle exceptions; exceptions need to be managed with `try-except`.
for i in range(5):
    try:
        if i == 2:
            raise ValueError("Error")
    except ValueError:
        continue
    print(i)  # Outputs 0, 1, 3, 4

# Summary:
# The for loop iterates over the numbers from 0 to 4.
# When i is 2, a ValueError is raised, caught by the except block, and the loop continues to the next iteration without executing the print statement.
# For all other values of i, the print statement is executed, resulting in the output: 0, 1, 3, 4.
# Output:
# 0
# 1
# 3
# 4
# The code demonstrates how the continue statement can be used in conjunction with exception handling to skip specific iterations of a loop.

### 19. How can `return` be used to set default values in a function?
# - Explanation: `return` can be used to provide default values when certain conditions are not met.
def get_value(value=None):
    if value is None:
        return "Default value"
    return value

print(get_value())          # Output: Default value
print(get_value("Custom"))  # Output: Custom
# Output:
# Default value
# Custom

### 20. How do `break` and `return` differ in their effect on loop execution?
# - Explanation: `break` exits the loop, while `return` exits the function containing the loop.
def loop_with_break():
    for i in range(5):
        if i == 3:
            break
        print(f"Break loop: {i}")

def loop_with_return():
    for i in range(5):
        if i == 3:
            return
        print(f"Return loop: {i}")

loop_with_break()  # Output: Break loop: 0, 1, 2
loop_with_return()  # Output: Return loop: 0, 1, 2

# Output:
# Break loop: 0
# Break loop: 1
# Break loop: 2
# Return loop: 0
# Return loop: 1
# Return loop: 2

# These examples and explanations demonstrate the practical uses and behaviors of `break`, `continue`, and `return` in various scenarios.
