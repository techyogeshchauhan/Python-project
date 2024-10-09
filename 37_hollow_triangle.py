def hollow_triangle_pattern(n):
    """
    Prints a hollow triangle star pattern of size n.
    
    Parameters:
        n (int): The number of rows in the triangle.
    """
    for i in range(n):
        # Print stars on the first and last positions of each row or on the bottom row
        for j in range(i + 1):
            if j == 0 or j == i or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")  # Print space in the hollow part
        print()  # Move to the next line after each row

# Example usage
size = 5
hollow_triangle_pattern(size)
    