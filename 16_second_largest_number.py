def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two elements"
    
    # Initialize the largest and second-largest
    first = second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    
    return second if second != float('-inf') else "No second largest element"

# Example usage
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
result = find_second_largest(numbers)
print("The second-largest element is:", result)
