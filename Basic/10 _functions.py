# Functions

def my_function(x, y):
    """
    This function takes two arguments and returns their sum.
    
    Parameters:
    x (int, float): The first number.
    y (int, float): The second number.
    
    Returns:
    int, float: The sum of x and y.
    """
    return x + y

my_result = my_function(5, 10)
print(f"The result of my_function is: {my_result}")  # Output: The result of my_function is: 15

def print_name(name, surname):
    print(f"Hello, {name} {surname}!")

print_name(surname="Doe", name="John")  # Output: Hello, John Doe!

# Function with default argument
def print_name_with_default(name, surname="Smith"):
    print(f"Hello, {name} {surname}!")

print_name_with_default(name="John")  # Output: Hello, John Smith!

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hello", "World", "from", "Python")  # Output: Hello World from Python