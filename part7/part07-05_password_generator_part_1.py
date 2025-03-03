import string
import random

def generate_password(size: int):
    password = ""
    for letter in range(size):
        password += random.choice(string.ascii_lowercase)
    return password


if __name__ == "__main__":
   for i in range(10):
    print(generate_password(8))