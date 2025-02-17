def histogram(my_word: str):
    words = {}
    for word in my_word:
        if word not in words:
            words[word] = 0
        words[word] += 1 
    
    for letter in words:
        stars = words[letter] * "*" 
        print(f"{letter} {stars}") 
 
if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")
 