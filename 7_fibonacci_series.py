# Get the limit from the user
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series using a for loop
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
