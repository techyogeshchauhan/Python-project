# Function to find the frequency of each element in a list
def find_frequency(lst):
    # Initialize an empty dictionary to store frequencies
    frequency_dict = {}

    # Loop through each element in the list
    for element in lst:
        # If the element is already in the dictionary, increment its count
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            # Otherwise, add the element to the dictionary with a count of 1
            frequency_dict[element] = 1

    return frequency_dict

# Example usage
sample_list = [2, 4, 6, 2, 8, 4, 2, 6, 8, 8]

# Call the function and store the result
result = find_frequency(sample_list)

# Display the frequency of each element
print("Frequency of each element:")
for element, frequency in result.items():
    print(f"{element}: {frequency}")
