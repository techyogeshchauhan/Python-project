import random
import string

def generate_password(length):
    """
    Generate a random password with a specified length.

    Parameters:
        length (int): The length of the password.

    Returns:
        str: A randomly generated password.
    """
    if length < 4:
        print("Password length should be at least 4 for security.")
        return None
    
    # Create a list of characters for the password (uppercase, lowercase, digits, and punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]
    
    # Fill the remaining length of the password with random characters from the combined pool
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the result to make the password unpredictable
    random.shuffle(password)
    
    # Convert the list of characters into a string
    return ''.join(password)

# Example usage
length = int(input("Enter the desired password length: "))
password = generate_password(length)

if password:
    print(f"Your randomly generated password is: {password}")
