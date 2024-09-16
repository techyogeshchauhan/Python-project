# Get a number from the user
num = int(input("Enter the number for the multiplication table: "))

# Generate and display the multiplication table
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
