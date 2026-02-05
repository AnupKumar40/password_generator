import random
import string

print("===================================")
print("     RANDOM PASSWORD GENERATOR     ")
print("===================================")

# Taking password length
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0")
        else:
            break
    except:
        print("Please enter a valid number")

# User choices
use_letters = input("Include letters (a-z, A-Z)? (y/n): ").lower()
use_numbers = input("Include numbers (0-9)? (y/n): ").lower()
use_symbols = input("Include symbols (!@#$)? (y/n): ").lower()

characters = ""

if use_letters == "y":
    characters += string.ascii_letters
if use_numbers == "y":
    characters += string.digits
if use_symbols == "y":
    characters += string.punctuation

# Validation
if characters == "":
    print("\nError: No character set selected!")
    print("Please select at least one option.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n-------------------------------")
    print("Generated Password:")
    print(password)
    print("-------------------------------")

