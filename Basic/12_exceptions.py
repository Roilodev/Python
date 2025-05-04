# Exceptions Handling
# Exceptions are errors that occur during the execution of a program.
# They can be caused by various reasons, such as invalid input, file not found, etc.
# In Python, exceptions are handled using try and except blocks.
# When an exception occurs, the code inside the try block is skipped and the code inside the except block is executed.
# You can also use else and finally blocks to handle exceptions in a more controlled way.
# The else block is executed if no exceptions occur in the try block.
# The finally block is always executed, regardless of whether an exception occurred or not.
# You can also raise exceptions manually using the raise statement.
# This can be useful for creating custom exceptions or for re-raising exceptions that you have caught.
# Example of exception handling

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution of divide_numbers function completed.")

divide_numbers(10, 2)  # Should print "Division successful!" and return 5.0
divide_numbers(10, 0)  # Should print "Error: Division by zero is not allowed." and return None