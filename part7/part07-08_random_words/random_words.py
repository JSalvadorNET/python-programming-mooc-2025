import string
import random
from random import choice, randint

def words(n: int, beginning: str):
    
    with open("words.txt", "r") as new_file:
        word_list = []
        for line in new_file:
            line = line.strip()
            word_list.append(line)

    matching_words = []
    for word in word_list:
        if word.startswith(beginning):
            matching_words.append(word)
    
    if len(matching_words) < n:
        raise ValueError("There are not enough words beginning with the specified string.")

    return random.sample(matching_words, n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
    print()
    word_list = words(5, "de")
    for word in word_list:
        print(word)
    print()
    word_list = words(12, "tog")
    for word in word_list:
        print(word)
