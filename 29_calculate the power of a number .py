def power(base, exp):
    """
    Recursively calculates the power of a number (base^exp).
    
    Parameters:
        base (float): The base number.
        exp (int): The exponent.
    
    Returns:
        float: The result of base^exp.
    """
    # Base case: Any number raised to the power of 0 is 1
    if exp == 0:
        return 1
    # If the exponent is negative, compute the reciprocal
    if exp < 0:
        return 1 / power(base, -exp)
    
    # Exponentiation by squaring
    half_power = power(base, exp // 2)
    
    # If the exponent is even, we can square the half power
    if exp % 2 == 0:
        return half_power * half_power
    # If the exponent is odd, we multiply by the base once more
    else:
        return base * half_power * half_power

# Example usage
base = 2
exp = 10
result = power(base, exp)
print(f"{base}^{exp} = {result}")
