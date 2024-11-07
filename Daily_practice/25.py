Here are 10 tricky, practical interview questions focused on Object-Oriented Programming (OOP) in Python:

### 1. **Creating a Singleton Class in Python**
   **Question:** How would you implement a singleton pattern in Python to ensure only one instance of a class is created?

   ```python
   class Singleton:
       _instance = None

       def __new__(cls, *args, **kwargs):
           if not cls._instance:
               cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
           return cls._instance

   # Example usage
   s1 = Singleton()
   s2 = Singleton()
   print(s1 == s2)  # Output: True
   ```

### 2. **Method Overloading in Python**
   **Question:** Python does not support method overloading like other languages. How would you simulate method overloading?

   ```python
   class OverloadExample:
       def add(self, *args):
           return sum(args)

   # Example usage
   obj = OverloadExample()
   print(obj.add(1, 2))  # Output: 3
   print(obj.add(1, 2, 3))  # Output: 6
   ```

### 3. **Multiple Inheritance and Method Resolution Order (MRO)**
   **Question:** How does Python resolve method calls when multiple inheritance is involved? Demonstrate this with an example.

   ```python
   class A:
       def show(self):
           print("A")

   class B(A):
       def show(self):
           print("B")

   class C(A):
       def show(self):
           print("C")

   class D(B, C):
       pass

   # Example usage
   obj = D()
   obj.show()  # Output: B
   print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
   ```

### 4. **Abstract Base Classes (ABCs)**
   **Question:** How would you create an abstract base class in Python, and why would you use one?

   ```python
   from abc import ABC, abstractmethod

   class Animal(ABC):
       @abstractmethod
       def sound(self):
           pass

   class Dog(Animal):
       def sound(self):
           return "Bark"

   # Example usage
   dog = Dog()
   print(dog.sound())  # Output: Bark
   ```

### 5. **Overriding `__str__` and `__repr__`**
   **Question:** What is the difference between `__str__` and `__repr__` methods? How would you override them in a class?

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __str__(self):
           return f"Person: {self.name}, {self.age}"

       def __repr__(self):
           return f"Person(name={self.name!r}, age={self.age!r})"

   # Example usage
   p = Person("John", 30)
   print(str(p))  # Output: Person: John, 30
   print(repr(p))  # Output: Person(name='John', age=30)
   ```

### 6. **Class-Level vs. Instance-Level Attributes**
   **Question:** Explain and demonstrate the difference between class-level attributes and instance-level attributes in Python.

   ```python
   class MyClass:
       class_attr = 0

       def __init__(self):
           self.instance_attr = 0

   # Example usage
   obj1 = MyClass()
   obj2 = MyClass()

   obj1.class_attr = 10
   obj1.instance_attr = 20

   print(obj1.class_attr, obj1.instance_attr)  # Output: 10 20
   print(obj2.class_attr, obj2.instance_attr)  # Output: 0 0
   ```

### 7. **Property Decorators and Getters/Setters**
   **Question:** How would you use property decorators to control access to a class attribute? Provide an example.

   ```python
   class Employee:
       def __init__(self, name, salary):
           self._name = name
           self._salary = salary

       @property
       def salary(self):
           return self._salary

       @salary.setter
       def salary(self, value):
           if value < 0:
               raise ValueError("Salary cannot be negative")
           self._salary = value

   # Example usage
   emp = Employee("John", 5000)
   emp.salary = 6000  # Setter invoked
   print(emp.salary)  # Output: 6000
   ```

### 8. **Dynamic Method Creation**
   **Question:** How can you dynamically add a method to a class or an instance at runtime?

   ```python
   class MyClass:
       pass

   def dynamic_method(self):
       return "This is a dynamic method"

   # Adding method to a single instance
   obj = MyClass()
   obj.dynamic_method = dynamic_method.__get__(obj)
   print(obj.dynamic_method())  # Output: This is a dynamic method

   # Adding method to the class
   MyClass.dynamic_method = dynamic_method
   another_obj = MyClass()
   print(another_obj.dynamic_method())  # Output: This is a dynamic method
   ```

### 9. **Enforcing Class Constraints Using `__init__` and `__new__`**
   **Question:** How would you enforce that a class can only be instantiated with specific arguments using the `__init__` or `__new__` methods?

   ```python
   class PositiveNumber:
       def __new__(cls, value):
           if value <= 0:
               raise ValueError("Only positive numbers are allowed")
           return super(PositiveNumber, cls).__new__(cls)

       def __init__(self, value):
           self.value = value

   # Example usage
   pos_num = PositiveNumber(10)  # Works fine
   # pos_num = PositiveNumber(-10)  # Raises ValueError
   ```

### 10. **Custom Metaclass to Control Class Creation**
   **Question:** How would you create a custom metaclass in Python to control the creation of classes?

   ```python
   class Meta(type):
       def __new__(cls, name, bases, dct):
           if "required_method" not in dct:
               raise TypeError(f"Class {name} must define 'required_method'")
           return super(Meta, cls).__new__(cls, name, bases, dct)

   class MyClass(metaclass=Meta):
       def required_method(self):
           return "This is required"

   # Example usage
   obj = MyClass()
   print(obj.required_method())  # Output: This is required

   # Uncommenting the following would raise a TypeError:
   # class AnotherClass(metaclass=Meta):
   #     pass
   ```

These questions will test both the conceptual understanding and practical implementation skills of OOP principles in Python. Each question is designed to challenge the interviewee's ability to apply OOP concepts in real-world scenarios.