def same_chars(word, char1, char2):
    if char1 < 0 or char2 < 0 or char1 >= len(word) or char2 >= len(word):
        return False
    return word[char1] == word[char2]
    
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
    print(same_chars("programmer", 0, 4))
    print(same_chars("programmer", 0, 12)) 