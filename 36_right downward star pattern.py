def right_downward_star_pattern(n):
    """
    Prints a right-aligned downward triangle star pattern of size n.
    
    Parameters:
        n (int): The number of stars in the first row and the height of the triangle.
    """
    for i in range(n, 0, -1):
        # Print leading spaces
        print("  " * (n - i), end="")
        # Print i stars in each row
        print("* " * i)

# Example usage
size = 5
right_downward_star_pattern(size)
