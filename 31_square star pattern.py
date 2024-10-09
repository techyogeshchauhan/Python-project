def square_star_pattern(n):
    """
    Prints a square star pattern of size n x n.
    
    Parameters:
        n (int): The size of the square (number of rows and columns).
    """
    for i in range(n):
        for j in range(n):
            print("*", end=" ")  # Print star followed by a space
        print()  # Move to the next line after each row

# Example usage
size = 5
square_star_pattern(size)
