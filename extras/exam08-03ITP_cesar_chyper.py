def caesar_encrypt(text: str, shift_value: int):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    new_word = ""
    
    for letter in text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_value) % len(alphabet)
            new_word += alphabet[new_position]
        else:
            new_word += letter
    
    return new_word
    
def caesar_decrypt(text: str, shift_value: int):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    new_word = ""
    
    for letter in text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) - shift_value) % len(alphabet)
            new_word += alphabet[new_position]
        else:
            new_word += letter
    
    return new_word

