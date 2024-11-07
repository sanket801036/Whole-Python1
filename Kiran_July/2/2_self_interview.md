### Interview Questions and Answers
1.What is a class in Python?
A class is a blueprint for creating objects.
   class Dog: 
       def __init__(self, name, age):
           self.name = name
           self.age = age
       def bark(self):
           return "Woof!"

2. **How do you create an object from a class in Python?**
  You create an object by calling the class as if it were a function, passing any required   arguments to the `__init__` method.
   my_dog = Dog(name="Buddy", age=5)

3. **What is the purpose of the `__init__` method in a class?**
   * The `__init__` method is the constructor method that initializes the objects.
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

4. **Explain the difference between instance variables and class variables.**
    Instance variables are unique to each instance of a class, whereas class variables are shared among all instances of the class.

   class Person:
       species = "Homo sapiens"  # Class variable

       def __init__(self, name):
           self.name = name  # Instance variable
   ```

7. **How do you define a method within a class?**

   **Answer:** Methods within a class are defined similarly to functions, but they include `self` as the first parameter to access instance variables.
   class Calculator:
       def add(self, a, b):
           return a + b

11. **How do you implement method overloading in Python?**
     Python does not support method overloading in the traditional sense. Instead, you can use default arguments or variable-length arguments.

    ```python
    class Math:
        def add(self, a, b, c=0):
            return a + b + c
    ```

12. **What is method overriding?**
    Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
    ```python
    class Animal:
        def speak(self):
            return "Animal sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"
    ```

13. **How do you use the `super()` function?**
    The `super()` function is used to call methods from a superclass in a subclass, allowing you to extend or modify behavior.

    ```python
    class Animal:
        def speak(self):
            return "Animal sound"

    class Dog(Animal):
        def speak(self):
            return super().speak() + " and Woof!"
    ```

14. **What are class methods and static methods?**
    **Answer:** Class methods receive the class itself as the first argument (usually `cls`) and can modify class state. Static methods do not receive any special first argument and work like regular functions.

    ```python
    class MyClass:
        class_variable = "Class variable"

        @classmethod
        def class_method(cls):
            return cls.class_variable

        @staticmethod
        def static_method():
            return "Static method"
    ```

    ```

16. **How can you ensure that an object is immutable in Python?**
    **Answer:** You can ensure immutability by using immutable data structures (e.g., tuples) and providing no methods that modify the object's state.

    ```python
    class ImmutablePoint:
        def __init__(self, x, y):
            self._x = x
            self._y = y

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y
    ```

18. **What is the purpose of the `__str__` and `__repr__` methods in Python?**

    **Answer:** The `__str__` method provides a human-readable string representation of an object, while `__repr__` provides an unambiguous string representation for debugging.

    ```python
    class Person:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Person named {self.name}"

        def __repr__(self):
            return f"Person(name={self.name!r})"
    ```


    ```

