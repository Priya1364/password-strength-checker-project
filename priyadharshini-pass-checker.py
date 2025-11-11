# Basic Password Strength Checker
# Author: Priyadharshini L
# File Name: priyadharshini-pass-checker.py

def check_password_strength(password):
    # Initialize strength counter
    strength = 0

    # Condition 1: Check password length
    if len(password) >= 8:
        strength += 1

    # Condition 2: Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        strength += 1

    # Condition 3: Check for lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        strength += 1

    # Condition 4: Check for uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        strength += 1

    # Condition 5: Check for special character
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if has_special:
        strength += 1

    # Determine strength category
    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"


# Main Program
def main():
    print("----- Basic Password Strength Checker -----")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print("Password Strength:", result)


# Run the main function
if __name__ == "__main__":
    main()
