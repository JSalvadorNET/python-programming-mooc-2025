my_dictionary = {}
 
while True:
    op = int(input("command (1 search, 2 add, 3 quit): "))
    if op == 3: # quit
        print("quitting...")
        break   
    elif op == 1: # search
        name = input("name: ")
        if name in my_dictionary:
            for number in my_dictionary[name]: 
                print(number)
        else:
            print("no number")     
    elif op == 2: # add 
        name = input("name: ")
        number = input("number: ")
        if name not in my_dictionary:
            my_dictionary[name] = []  
        my_dictionary[name].append(number)  
        print("ok!")
 