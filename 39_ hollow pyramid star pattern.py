def hollow_pyramid_star_pattern(n):
    """
    Prints a hollow pyramid star pattern of size n.
    
    Parameters:
        n (int): The number of rows in the pyramid.
    """
    for i in range(1, n + 1):
        # Print spaces for the left alignment
        print(" " * (n - i), end="")
        
        # For the first row and last row, print all stars
        if i == 1 or i == n:
            print("* " * i)
        else:
            # Print stars at the first and last positions of the row
            print("*", end=" ")
            # Print spaces in between for hollow effect
            print("  " * (i - 2), end="")
            # Print the last star in the row
            print("*")

# Example usage
size = 5
hollow_pyramid_star_pattern(size)
