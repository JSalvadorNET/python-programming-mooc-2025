phrase = ""
last_word = ""
word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last_word:
        print(phrase)
        break
    else:
        if phrase:  
            phrase += " " + word
        else:
            phrase += word  
        last_word = word