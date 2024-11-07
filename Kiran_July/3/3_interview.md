### **Instance Variables**
Instance variables are variables that are bound to a specific #instance of a class. They are used to store data that is unique #to each object created from the class. Instance variables are #defined within methods using the `self` keyword.

**Characteristics:**
- Each object (instance) of the class has its own copy of the instance variables.
- They are created when an instance is initialized and can be modified by instance methods.
- They are defined inside methods, typically in the constructor (`__init__` method) of the class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"

# Creating instances of Dog
dog1 = Dog("Rex", 5)
dog2 = Dog("Buddy", 3)

print(dog1.name)  # Output: Rex
print(dog2.name)  # Output: Buddy
```

In the example above, `name` and `age` are instance variables. Each `Dog` object has its own `name` and `age`.

### **Class Variables**

**Definition:**
Class variables are variables that are shared across all instances of a class. They are defined within the class but outside of any instance methods. Class variables are used to store data that should be shared among all instances.

**Characteristics:**
- They are shared by all instances of the class.
- They are defined directly within the class scope, not inside any methods.
- They can be accessed using the class name or through instances, but changes to class variables are reflected across all instances.

**Example:**

```python
class Dog:
    species = "Canis lupus familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"

# Creating instances of Dog
dog1 = Dog("Rex", 5)
dog2 = Dog("Buddy", 3)

print(Dog.species)  # Output: Canis lupus familiaris
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris

# Changing the class variable
Dog.species = "Canis lupus"
print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis lupus
```

In this example, `species` is a class variable shared by all instances of the `Dog` class. Changes to `species` affect all instances, as demonstrated by updating the value through the class name.

### **Summary:**

- **Instance Variables:** Unique to each instance, defined using `self`, and typically initialized in the `__init__` method.
- **Class Variables:** Shared across all instances, defined within the class scope, and can be accessed using either the class name or instances.

Understanding the distinction between these two types of variables is crucial for managing state and behavior in object-oriented programming.