def find_allowed(wordlist, minimum):

    desired_letters = "aeiouy"

    allowed_words = []

    for word in wordlist:
        count = sum(1 for char in word if char in desired_letters)
        if count >= minimum:
            allowed_words.append(word)

    return allowed_words

if __name__ == "__main__":
    wordlist = ["apple", "banana", "cherry", "orange", "peach", "pineapple"]
    minimum = 3
    result = find_allowed(wordlist, minimum)
    print(result)  ['banana', 'orange', 'pineapple']
    
    
