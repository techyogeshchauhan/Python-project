def hollow_star_pattern(n):
    """
    Prints a hollow square star pattern of size n x n.
    
    Parameters:
        n (int): The size of the square (number of rows and columns).
    """
    for i in range(n):
        for j in range(n):
            # Print stars at the borders (first and last row, or first and last column)
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")  # Print space inside the square
        print()  # Move to the next line after each row

# Example usage
size = 5
hollow_star_pattern(size)
