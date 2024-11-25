import random
import string

def check_password_strength(password):

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter."

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter."

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."

    if not any(c in string.punctuation for c in password):
        return False, "Password must contain at least one special character."

    return True, "Strong password."



def suggest_strong_password(base_word):
    
    special_chars = string.punctuation
    # Ensure at least one uppercase letter
    password = ''.join(
        random.choice((char.upper(), char.lower())) if char.isalpha() else char
        for char in base_word
    )

    # Insert a special character at a random position
    pos_special = random.randint(1, len(password) - 1)
    password = password[:pos_special] + random.choice(special_chars) + password[pos_special:]

    # Insert a digit at a random position
    pos_digit = random.randint(1, len(password))
    password = password[:pos_digit] + str(random.randint(0, 9)) + password[pos_digit:]

    return password


user_password = input("Enter a password to check: ")
is_strong, message = check_password_strength(user_password)

if is_strong:
    print("Password is strong.")
else:
    print(f"Weak password: {message}")
    base_word = input("Enter a base word for password suggestions: ")
    print("Suggested strong passwords:")
    for _ in range(3):  # Suggest three passwords
        print(suggest_strong_password(base_word))
