import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password should be at least 4 characters long."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))
