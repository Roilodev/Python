# Error types

# SyntaxError
# print("Hello World"  # Missing closing parenthesis

# NameError
# print(hello)  # hello is not defined

# TypeError
# print("Hello" + 5)  # Cannot concatenate str and int

# ValueError
# int("Hello")  # Cannot convert string to int

# IndexError
# my_list = [1, 2, 3]
# print(my_list[5])  # Index out of range

# KeyError
# my_dict = {"name": "Alice"}
# print(my_dict["age"])  # Key 'age' not found in dictionary

# AttributeError
# class MyClass:
#     def my_method(self):
#         pass
# my_instance = MyClass()
# my_instance.non_existent_method()  # Method does not exist

# ImportError
# from math import non_existent_function  # Function does not exist in math module

# ZeroDivisionError
# print(5 / 0)  # Division by zero

# FileNotFoundError
# with open("non_existent_file.txt", "r") as file:  # File does not exist
#     content = file.read()
# print(content)

# IndentationError
# def my_function():
# print("Hello")  # Missing indentation
# my_function()

# UnboundLocalError
# def my_function():
#     print(x)  # x is referenced before assignment
#     x = 10
# my_function()

# ModuleNotFoundError
# import non_existent_module  # Module does not exist

# RecursionError
# def recursive_function():
#     return recursive_function()  # Infinite recursion
# recursive_function()

