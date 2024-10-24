# Function to print a right triangle star pattern
def right_triangle_star_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# Example usage
n = int(input("Enter the number of rows: "))
right_triangle_star_pattern(n)
