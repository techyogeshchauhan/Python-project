def merge_sorted_lists(list1, list2):
    # Initialize an empty list to store the merged result
    merged_list = []
    
    # Initialize pointers for both lists
    i, j = 0, 0
    
    # Loop through both lists and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # If there are any remaining elements in list1, add them to merged_list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # If there are any remaining elements in list2, add them to merged_list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_sorted_lists(list1, list2)
print(result)
