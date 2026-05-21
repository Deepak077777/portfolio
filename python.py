import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    print("\n--- Password Generator ---")
    
    length = int(input("Enter password length: "))
    
    if length < 4:
        print("Password length should be at least 4.")
        continue

    password = generate_password(length)
    print("Generated Password:", password)

    again = input("Generate another? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break