def sort_dicts_by_key(dict_list, key):
    """
    Sorts a list of dictionaries by a specific key.

    Parameters:
        dict_list (list): List of dictionaries to sort.
        key (str): The key in the dictionaries to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        return sorted(dict_list, key=lambda x: x[key])
    except KeyError:
        print(f"Error: One or more dictionaries do not have the key '{key}'")
        return dict_list

# Example list of dictionaries
students = [
    {"Name": "Aarav", "Score": 87},
    {"Name": "Vivaan", "Score": 78},
    {"Name": "Aditya", "Score": 92},
    {"Name": "Vihaan", "Score": 85},
    {"Name": "Krishna", "Score": 82}
]

# Sort by 'Score'
sorted_students = sort_dicts_by_key(students, 'Score')

# Display sorted list
print("Sorted by Score:")
for student in sorted_students:
    print(student)

# Sort by 'Name'
sorted_students = sort_dicts_by_key(students, 'Name')

# Display sorted list
print("\nSorted by Name:")
for student in sorted_students:
    print(student)
