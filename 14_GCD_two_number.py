def gcd(a, b):
    # Implementing the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
result = gcd(num1, num2)

# Display the result
print("The greatest common divisor of", num1, "and", num2, "is:", result)
