def hollow_diamond_star_pattern(n):
    """
    Prints a hollow diamond star pattern with n rows (upper half and lower half combined).
    
    Parameters:
        n (int): The number of rows in the upper half of the diamond.
    """
    # Upper half of the hollow diamond
    for i in range(1, n + 1):
        # Print spaces for left alignment
        print(" " * (n - i), end="")
        # Print stars at the boundaries of the diamond
        if i == 1:
            print("*")
        else:
            print("*", end="")
            print(" " * (2 * i - 3), end="")
            print("*")
    
    # Lower half of the hollow diamond
    for i in range(n - 1, 0, -1):
        # Print spaces for left alignment
        print(" " * (n - i), end="")
        # Print stars at the boundaries of the diamond
        if i == 1:
            print("*")
        else:
            print("*", end="")
            print(" " * (2 * i - 3), end="")
            print("*")

# Example usage
size = 5
hollow_diamond_star_pattern(size)
