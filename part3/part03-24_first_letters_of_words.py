sentence = input("Please type in a sentence: ")
sentence_split = sentence.split()

for word in sentence_split:
    print(word[0])