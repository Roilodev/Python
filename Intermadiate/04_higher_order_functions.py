# Higher order functions

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add_one(1, 2, sum_one))  # Output: 4

# Closures
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier_of(2)
triple = make_multiplier_of(3)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15

def sum_ten(a):
    def add(value):
        return value + 10 + a
    return add

add_closure = sum_ten(2)
print(add_closure(5))  # Output: 15

sum_ten(2)(5)  # Output: 17

# Bilt-in functions

numbers = [1, 2, 3, 4, 5, 6]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))  # Output: [2, 4, 6, 8, 10]
print(list(map(lambda number: number * 2, numbers)))  # Output: [2, 4, 6, 8, 10]

# Filters
def is_even(number):
    return number % 2 == 0

print(list(filter(is_even, numbers)))  # Output: [2, 4]

# Usando Lambda
print(list(filter(lambda number: number % 2 == 0, numbers)))  # Output: [2, 4]

# Reduce
from functools import reduce

def sum_two_numbers(a, b):
    return a + b

print(reduce(sum_two_numbers, numbers))  # Output: 21
print(reduce(lambda a, b: a + b, numbers))  # Output: 21

