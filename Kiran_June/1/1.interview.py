"""
Laptop = {"lenovo":{"lenovo_V15":{"Generation":"i3","Ram":"4gb","SSD":"512GB","Cores":6},"Lenovo_V14":{"Generation":"i5","Ram":"8gb","SSD":"1120GB","Cores":8}},"HP":{"HP_Chromebook":{"Generation":"i7","Ram":"12gb","SSD":"245GB","Cores":4},"HP_Pavillion":{"Generation":"i5","Ram":"18gb","SSD":"1125GB","Cores":12}}}
#What is dict?
It is  ordered,mutable,heterogeneous collection of elements where data is represented in the form of key and value.

#How to represent dict

In Python, a dictionary is represented using curly braces {}. It consists of key-value pairs, where the keys are unique and immutable, and the values can be of any data type.

Here's an example of how to represent a dictionary:
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

In the given code snippet, the dictionary Laptop is defined with nested dictionaries representing different laptop models and their specifications.""" 

d = {"name": "Alice", "age": 25}
age = d.get("age")
print(age)  # Output: 25