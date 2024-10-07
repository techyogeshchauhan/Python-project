import csv

# Function to read data from a CSV file
def read_csv(file_path):
    data = []
    try:
        # Open the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Strip any leading/trailing spaces from the headers and values
                row = {key.strip(): value.strip() for key, value in row.items()}
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Function to calculate the average score
def calculate_average(data, column):
    total = 0
    count = 0
    for row in data:
        total += float(row[column])
        count += 1
    return total / count if count > 0 else 0

# Function to find the maximum value in a column
def find_max(data, column):
    max_value = float('-inf')
    max_row = None
    for row in data:
        if float(row[column]) > max_value:
            max_value = float(row[column])
            max_row = row
    return max_row

# Function to display all data
def display_data(data):
    for row in data:
        print(row)

# Example usage
file_path = 'students_scores.csv'  # Replace with your actual CSV file path

# Read the CSV file
data = read_csv(file_path)

# If data was successfully read, perform operations
if data:
    print("\nData from CSV file:")
    display_data(data)

    # Calculate average score
    average_score = calculate_average(data, 'Score')
    print(f"\nAverage score: {average_score}")

    # Find student with the maximum score
    max_score_row = find_max(data, 'Score')
    print(f"\nStudent with the highest score: {max_score_row['Name']} ({max_score_row['Score']})")
