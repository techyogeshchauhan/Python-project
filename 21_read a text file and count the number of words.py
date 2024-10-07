# Function to count the number of words in a text file
file_path = 'C:/Python project/21_sample.md'
def count_words_in_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Return the number of words
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0

# Example usage
file_path = 'sample.md'  # Replace with the path to your file
word_count = count_words_in_file(file_path)

# Display the word count
if word_count > 0:
    print(f"The number of words in the file '{file_path}' is: {word_count}")
