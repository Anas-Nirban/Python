import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak", "Password must be at least 8 characters long."
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak", "Include at least one uppercase letter (A-Z)."
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak", "Include at least one lowercase letter (a-z)."
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        return "Weak", "Include at least one number (0-9)."
    
    # Check for special symbols
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak", "Include at least one special symbol (!@#$%^&*(),.?\":{}|<>)."
    
    # If the password meets all the requirements
    if len(password) >= 12:
        return "Strong", "Great job! Your password is strong."
    else:
        return "Medium", "Consider increasing the length for a stronger password."

print("Welcome to the Password Strength Checker!")

# Loop until a strong password is entered
while True:
    # Get user input
    user_password = input("\nEnter your password: ")
    
    # Check the strength of the password
    strength, feedback = check_password_strength(user_password)
    
    # Output the result
    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")
    
    # Break the loop if the password is strong
    if strength == "Strong":
        print("\nYour password is secure! You can use it safely.")
        break
    else:
        print("\nPlease try again to create a stronger password.")
