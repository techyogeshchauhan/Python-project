def reverse_pyramid_star_pattern(n):
    """
    Prints a reverse pyramid star pattern of size n.
    
    Parameters:
        n (int): The number of rows in the reverse pyramid.
    """
    for i in range(n, 0, -1):
        # Print spaces for left alignment
        print(" " * (n - i), end="")
        # Print stars in the current row
        print("* " * i)

# Example usage
size = 5
reverse_pyramid_star_pattern(size)
