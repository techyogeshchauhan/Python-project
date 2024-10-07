def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the target.

    Parameters:
        sorted_list (list): A list of sorted elements.
        target (int or float): The element to search for.

    Returns:
        int: The index of the target element if found, else -1.
    """
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        
        # Check if the target is present at mid
        if sorted_list[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif sorted_list[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # Target is not in the list
    return -1

# Example usage
sorted_list = [10, 22, 35, 40, 45, 57, 63, 75, 81, 99]
target = int(input("Enter the number you want to search for: "))

# Perform binary search
index = binary_search(sorted_list, target)

# Display the result
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the list.")
