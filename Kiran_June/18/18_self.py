# Certainly! Here are 20 interview questions on scope in Python along with their answers:

# 1. *What is variable scope in Python?*
#    - *Answer:* Variable scope refers to the region of code where a variable is visible or can be accessed. In Python, variables have either local or global scope.

# 2. *Explain the difference between local and global scope in Python.*
#    - *Answer:* 
#      - *Local scope:* Variables defined within a function have local scope. They can only be accessed within that function.
#      - *Global scope:* Variables defined outside of any function or in the global keyword scope have global scope. They can be accessed throughout the entire program.

# 3. *How do you define a variable with global scope inside a function?*
#    - *Answer:* Use the global keyword followed by the variable name inside the function to declare that the variable is global and not local to the function.

#      def my_function():
#          global x
#          x = 10
     

# 4. *What is the scope of a variable declared inside a function?*
#    - *Answer:* Variables declared inside a function have local scope. They are only accessible within the function where they are defined.

# 5. *Explain the concept of nested scope in Python.*
#    - *Answer:* Nested scope refers to the situation where a function is defined inside another function. The inner function has access to variables in the outer function's scope.
# Nested Scope in Python
# In Python, a scope refers to the region of the code where a variable is defined and accessible. Nested scope refers to the ability of Python to access variables from outer scopes in a nested function or block.

x = 10  # global scope
def outer():
    y = 20  # outer scope
    def inner():
        z = 30  # inner scope
        print("Inner scope:", x, y, z)
    inner()
    print("Outer scope:", x, y)
outer()
print("Global scope:", x)

# x is defined in the global scope and is accessible from all scopes.
# y is defined in the outer scope and is accessible from the inner scope.
# z is defined in the inner scope and is only accessible within that scope.
# When we run this code, the output will be:

# Inner scope: 10 20 30
# Outer scope: 10 20
# Global scope: 10
# As you can see, the inner function can access variables from the outer and global scopes, but the outer function cannot access variables from the inner scope.

# How it works
# When Python looks up a variable, it follows the LEGB rule:*******************************************************
# Local: Looks for the variable in the current scope.
# Enclosing: Looks for the variable in the outer scopes.
# Global: Looks for the variable in the global scope.
# Builtin: Looks for the variable in the built-in scope (e.g., len, range, etc.).
# By following this rule, Python can resolve variable references in a nested scope

# 6. *How does Python handle variable scope in nested functions?*

#    - *Answer:* Python uses a concept called closure to handle variable scope in nested functions. Inner functions can access variables from outer functions but cannot modify them unless using nonlocal.

# Variable Scope in Nested Functions in Python
# Python handles variable scope in nested functions using a concept called closure. Inner functions can access variables from outer functions, but they cannot modify them unless they use the nonlocal keyword.

def outer():
    x = 10  # outer scope

    def inner():
        print("Inner scope:", x)  # access x from outer scope

    inner()
    print("Outer scope:", x)

outer()

# Inner scope: 10
# Outer scope: 10
# As you can see, the inner function can access the variable x from the outer scope.

# Modifying Variables
# If we try to modify the variable x in the inner function, it will create a new local variable x instead of 
# modifying the outer scope variable x.

def outer():
    x = 10  # outer scope

    def inner():
        x = 20  # creates a new local variable x
        print("Inner scope:", x)

    inner()
    print("Outer scope:", x)

outer()
# Inner scope: 20
# Outer scope: 10
# As you can see, the inner function created a new local variable x instead of modifying the outer scope variable x.

# Using nonlocal
# To modify the variable x in the outer scope, we can use the nonlocal keyword.

def outer():
    x = 10  # outer scope

    def inner():
        nonlocal x  # refer to x in the outer scope
        x = 20  # modify x in the outer scope
        print("Inner scope:", x)

    inner()
    print("Outer scope:", x)

outer()

# Inner scope: 20
# Outer scope: 20
# As you can see, the inner function modified the variable x in the outer scope using the nonlocal keyword.



# 7. *What is a global variable? Give an example.*
#    - *Answer:* A global variable is a variable declared outside of any function or in the global scope. It can be accessed from any part of the program.
#      python
#      x = 10  # global variable

#      def my_function():
#          print(x)  # accessing global variable

#      my_function()
     

# 8. *How can you modify a global variable inside a function?*
#    - *Answer:* To modify a global variable inside a function, you need to use the global keyword to declare the variable as global within the function.
#      python
#      x = 10

#      def modify_global():
#          global x
#          x = 20

#      modify_global()
#      print(x)  # Output: 20
     

# 9. *Explain the concept of nonlocal variables in Python.*
#    - *Answer:* Nonlocal variables are used in nested functions to access variables from the nearest enclosing scope (outer function) that is not global. They are declared using the nonlocal keyword.
#      def outer_function():
#          x = 10  # outer function variable

#          def inner_function():
#              nonlocal x
#              x += 5
#              print(x)  # accessing and modifying outer function variable

#          inner_function()

#      outer_function()  # Output: 15
     

# 10. *Discuss the LEGB rule for variable resolution in Python.*
#     - *Answer:* The LEGB rule stands for Local, Enclosing (nonlocal), Global, and Built-in scopes. It defines the order in which Python searches for names (variables) when they are referenced.

# 11. *What happens if a variable is defined both globally and locally with the same name?*
#     - *Answer:* If a variable is defined both globally and locally with the same name, the local variable takes precedence within its scope. To access the global variable, you can use the global keyword or refer to it using the module name.

# 12. *Explain the scope of function parameters in Python.*
#     - *Answer:* Function parameters have local scope within the function where they are defined. They are accessible only within the function and do not exist outside of it.

# 13. *How does Python handle scope in lambda functions?*
#     - *Answer:* Lambda functions can access variables in their enclosing scope (like nonlocal variables in nested functions). However, they cannot modify variables from the enclosing scope unless using nonlocal.

# 14. *What is the scope of variables imported from modules in Python?*
#     - *Answer:* Variables imported from modules have module-level scope. They can be accessed within the module where they are imported, using the module name as a prefix.

# 15. *Explain the concept of global keyword in Python.*
# The global keyword in Python is used inside a function to declare that a variable refers to the global scope, rather than creating a new local variable with the same name.

# 16. *How can you create a closure in Python?*
#     - *Answer:* A closure in Python is created by defining a nested function that references variables from its enclosing scope. This allows the inner function to retain access to those variables even after the outer function has finished executing.

# 17. *Discuss the lifetime of variables in Python based on their scope.*
#     - *Answer:* 
#       - *Local variables:* Created when the function is called and destroyed when the function exits.
#       - *Global variables:* Created when the program starts and destroyed when the program ends.
#       - *Nonlocal variables:* Persist as long as the enclosing function is alive and are destroyed when the function exits.

# 18. *How can you debug scope-related issues in Python?*
#     - *Answer:* Use print statements to check variable values at different points in your code, especially within functions or loops where scope issues commonly occur. Debugging tools like pdb can also help trace variable values.

# 19. *Explain the concept of built-in scope in Python.*
#     - *Answer:* Built-in scope refers to names (like built-in functions and exceptions) that are available globally in all Python modules without needing to import them. Examples include print(), len(), and TypeError.

# 20. *What precautions should you take to avoid scope-related bugs in Python?*
#     - *Answer:* Avoid using global variables extensively; instead, use function parameters and return values to pass data between functions. Use proper naming conventions to avoid shadowing variables unintentionally, and understand the scope hierarchy (LEGB rule) thoroughly.

# These questions and answers cover various aspects of scope in Python, including local, global, nonlocal scopes, the LEGB rule, closures, and best practices to avoid scope-related issues in Python programming.