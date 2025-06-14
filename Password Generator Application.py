import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random password with specified complexity"""
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure at least one character from each selected character set
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def password_generator():
    print("\nSecure Password Generator")
    print("-------------------------")
    
    try:
        # Get password length
        while True:
            try:
                length = int(input("Enter password length (8-64): "))
                if 8 <= length <= 64:
                    break
                print("Password length must be between 8 and 64 characters.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get complexity options
        print("\nPassword Complexity Options:")
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate and display password
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {'Strong' if (use_uppercase and use_digits and use_special) else 'Medium' if (use_uppercase or use_digits or use_special) else 'Weak'}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    password_generator()