import random
import string


# 1️ Ask the user for password length

length = int(input("Enter the desired password length: "))


# 2️ Ask the user for password complexity level

print("\nChoose password complexity level:")
print("1. Less (only lowercase letters)")
print("2. Moderate (letters and numbers)")
print("3. Hard (letters, numbers, and special characters)")

choice = int(input("Enter 1, 2, or 3: "))


# 3️ Define possible characters based on complexity

if choice == 1:
    characters = string.ascii_lowercase
elif choice == 2:
    characters = string.ascii_letters + string.digits
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to Hard level.")
    characters = string.ascii_letters + string.digits + string.punctuation


# 4️ Generate the password

password = ''.join(random.choice(characters) for _ in range(length))


# 5️ Display the password

print("\nYour generated password is:", password)
