def diamond_star_pattern(n):
    """
    Prints a diamond star pattern with n rows (upper half and lower half combined).
    
    Parameters:
        n (int): The number of rows in the upper half of the diamond.
    """
    # Upper half of the diamond (Pyramid shape)
    for i in range(1, n + 1):
        # Print spaces for left alignment
        print(" " * (n - i), end="")
        # Print stars
        print("* " * i)
    
    # Lower half of the diamond (Inverted Pyramid shape)
    for i in range(n - 1, 0, -1):
        # Print spaces for left alignment
        print(" " * (n - i), end="")
        # Print stars
        print("* " * i)

# Example usage
size = 5
diamond_star_pattern(size)
