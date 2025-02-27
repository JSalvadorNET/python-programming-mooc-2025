def spellchecker(sentence):
    word_list = []
    words = sentence.split()
    correct_sentence = []
    
    with open ("wordlist.txt") as new_file:
        for line in new_file:
            word_list.append(line.strip().lower())
            
    for word in words:
        if word.lower() in word_list:
            correct_sentence.append(word)
        else:
            correct_sentence.append(f"*{word}*")
            
    for word in correct_sentence:
        print(word, end=" ")
    print()


user_input = input("Write text: ")  
spellchecker(user_input)