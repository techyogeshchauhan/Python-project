# # Get the number of rows from the user
# num_rows = int(input("Enter the number of rows: "))

# # Iterate over each row
# for i in range(1, num_rows + 1):
#     # Print '*' i times
#     for j in range(i):
#         print("*", end="")
#     # Move to the next line
#     print()
def left_triangle_pattern(n):
    """
    Prints a left-aligned triangle star pattern of size n.
    
    Parameters:
        n (int): The height of the triangle (number of rows).
    """
    for i in range(1, n+1):
        print("* " * i)

# Example usage
size = 5
left_triangle_pattern(size)
