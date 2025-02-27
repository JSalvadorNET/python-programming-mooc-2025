while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))
    if option == 0:
        print("Bye now!")
        break
    if option == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(entry + "\n")
        print("Diary saved")
    if option == 2:
        with open("diary.txt", "r") as my_file:
            read = my_file.read()
            print(read)
        
        
        