def matrix_multiplication(A, B):
    """
    Performs matrix multiplication of two matrices A and B.
    
    Parameters:
        A (list of list of ints/floats): The first matrix.
        B (list of list of ints/floats): The second matrix.
    
    Returns:
        list of list of ints/floats: The result of matrix multiplication A * B.
    """
    # Number of rows in A and B
    rows_A = len(A)
    cols_A = len(A[0])
    
    # Number of rows and columns in B
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Ensure the matrices can be multiplied (columns of A must equal rows of B)
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B since cols_A == rows_B
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example usage:
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Perform matrix multiplication
result = matrix_multiplication(A, B)

# Display the result
print("Result of A * B:")
for row in result:
    print(row)
