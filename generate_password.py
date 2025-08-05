# generate_password.py

import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols
    if not all_chars:
        return "❌ No character types selected."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def user_input():
    print("🔐 Heron Password Generator")
    try:
        length = int(input("Enter password length (e.g. 12): "))
    except ValueError:
        print("❌ Invalid number. Defaulting to 12.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\n✅ Your secure password:\n{password}")

if __name__ == "__main__":
    user_input()
