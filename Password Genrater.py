#Task-3: Password Generator

#Random module in Python provides functions for generating random numbers.
import random
#String function provides a ASCII character,s 
import string


# Python OOPs Concept
class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
# Creating an instance of PasswordGenerator
    password_generator = PasswordGenerator()

# display the user for the desired password length
#Using the try and except function of python
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

 # Generating and displaying the password
generated_password = password_generator.generate_password(length)
print("Generated Password:", generated_password)
