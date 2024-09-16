# Get the string from the user
string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for an accurate comparison
cleaned_string = string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
