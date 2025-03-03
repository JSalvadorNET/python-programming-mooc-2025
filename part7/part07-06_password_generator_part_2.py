import string
import random
from random import choice, randint

def generate_strong_password(size: int, number: bool, special_char: bool):
    password = ""
    special = "!?=+-()#"
    for _ in range(size):
        if number and special_char:
            password += random.choice(string.ascii_lowercase) + str(randint(1, 9)) + (random.choice(special)) 
        elif number:
            password += random.choice(string.ascii_lowercase) + str(randint(1, 9))
        elif special_char:
            password += random.choice(string.ascii_lowercase) + (random.choice(special)) 
        else:
            password += random.choice(string.ascii_lowercase)
    return password[:size]


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))