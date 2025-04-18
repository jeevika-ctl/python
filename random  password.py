import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
        else:
            pwd = generate_password(length)
            print(f"Generated password: {pwd}")
    except ValueError:
        print("Please enter a valid number.")
