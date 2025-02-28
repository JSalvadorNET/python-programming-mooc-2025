while True:
    print("1 - Add word, 2 - Search, 3 - Quit")  
    option = int(input("Function: ")) 
    if option == 3:
        print("Bye!")
        break  
    
    elif option == 1:
        word_f = input("The word in Finnish: ")
        word_i = input("The word in English: ")
        
        with open("dictionary.txt", "a") as new_file:
            new_file.write(f"{word_f};{word_i}\n") 
        
        print("Dictionary entry added")  

    elif option == 2:
        search_term = input("Search term: ").lower()
        found = False

        with open("dictionary.txt", "r") as file:
            for line in file:
                word_f, word_i = line.strip().split(";")
                
                if search_term in word_f.lower() or search_term in word_i.lower():
                    print(f"{word_f} - {word_i}")
                    found = True

        if found == False:
            print("No matches found.")
