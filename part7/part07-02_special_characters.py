import string

def separate_characters(my_string: str):
    ascii_letters = ""
    string_punctuation = ""
    other_chars = ""

    for c in my_string:
        if c in string.ascii_letters:
            ascii_letters += c
        elif c in string.punctuation:
            string_punctuation += c
        else:
            other_chars += c

    return ascii_letters, string_punctuation, other_chars
    
    
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
