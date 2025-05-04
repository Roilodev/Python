# Classes

# A class is a blueprint for creating objects. An object has properties (attributes) and behaviors (methods).
# A class is a collection of objects. A class is a blueprint for creating objects. An object has properties (attributes) and behaviors (methods).

class Person:
    def __init__(self, name, age , alias = "Sin alias"):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
        self.alias = alias  # Instance variable

    def get_name(self):
        return self.name

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

Mario = Person("Mario", 30, "El fontanero")
print(Mario.name)  # Accessing the instance variable
print(Mario.greet())  # Calling the method