word_list = []
 
while True:
    word = input("Word: ")
    if word in word_list:
        print(f"You typed in {len(word_list)} different words")
        break
    word_list.append(word)
    