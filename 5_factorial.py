# Get a number from the user
num = int(input("Enter a number: "))

# Initialize the factorial value
factorial = 1

# Calculate the factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Display the result
print("The factorial of", num, "is", factorial)

