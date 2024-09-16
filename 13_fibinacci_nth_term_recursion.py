def fibonacci(n):
    # Base cases
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get the term number from the user
n = int(input("Enter the term number for the Fibonacci series: "))

# Calculate and display the nth term
print(f"The {n}th term of the Fibonacci series is:", fibonacci(n))
