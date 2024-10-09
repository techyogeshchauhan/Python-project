def pyramid_star_pattern(n):
    """
    Prints a pyramid star pattern of size n.
    
    Parameters:
        n (int): The number of rows in the pyramid.
    """
    for i in range(1, n + 1):
        # Print spaces for the left alignment
        print(" " * (n - i), end="")
        # Print stars in the current row
        print("* " * i)

# Example usage
size = 5
pyramid_star_pattern(size)
