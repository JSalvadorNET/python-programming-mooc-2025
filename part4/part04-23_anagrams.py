def anagrams(word1,word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    if word1_sorted == word2_sorted:
        return True
    else:
        return False
    
 