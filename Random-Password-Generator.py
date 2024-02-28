import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Your new password is:", password)
