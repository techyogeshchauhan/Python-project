# Function to count the occurrences of each word in the given text
def count_word_occurrences(text):
    # Convert the text to lowercase and split it into words
    words = text.lower().split()

    # Initialize an empty dictionary to store word counts
    word_count = {}

    # Loop through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        else:
            # Otherwise, add the word to the dictionary with a count of 1
            word_count[word] = 1

    return word_count

# Example usage
sample_text = "This is a sample text. This text is a simple text."

# Remove punctuation from the text
import string
sample_text = sample_text.translate(str.maketrans('', '', string.punctuation))

# Call the function and store the result
result = count_word_occurrences(sample_text)

# Display the occurrences of each word
print("Word occurrences:")
for word, count in result.items():
    print(f"{word}: {count}")
