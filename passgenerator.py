import random
import string
import pyperclip

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def save_password(password, purpose, account, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(f"{purpose} | {account} | {password}\n")
    print(f"Password saved to {filename}")

# --- Main flow ---
length = int(input("Enter the desired password length (minimum 4): "))
pwd = generate_password(length)
print("The password is:", pwd)
pyperclip.copy(pwd)
print("Password copied to clipboard.")
save = input("Do you want to save the password? (yes/no): ").lower()
if save == 'yes':
    purpose = input("Enter the purpose of the password (e.g., email, social media): ")
    account = input("Enter the account/username associated with this password: ")
    save_password(pwd, purpose, account)
