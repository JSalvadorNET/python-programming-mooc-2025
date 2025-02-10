def first_word(word1):
    sentence_split = word1.split()
    return sentence_split[0]
    
def second_word(word2):
    sentence_split = word2.split()
    return sentence_split[1]
    
 
def last_word(last_word):
    sentence_split = last_word.split()
    return sentence_split[-1]
 
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    
 