import math

def calculate_factorial(n):
    """
    Calculate the factorial of a number using math module.

    Parameters:
        n (int): The number to calculate factorial of.

    Returns:
        int: The factorial of the number.
    """
    return math.factorial(n)

# Example usage
number = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial
result = calculate_factorial(number)

# Display result
print(f"The factorial of {number} is: {result}")
