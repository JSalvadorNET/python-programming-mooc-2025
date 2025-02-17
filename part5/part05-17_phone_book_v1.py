my_dictionary = {}
 
while True:
    op = int(input("command (1 search, 2 add, 3 quit): "))
    if op == 3:
        print("quitting...")
        break
    elif op == 1:
        name = input("name: ")
        if name in my_dictionary:
            print(my_dictionary[name])
        else:
            print("no number")
    elif op == 2:
        name = input("name: ")
        number = input("number: ")
        my_dictionary[name] = number
        print("ok!")
 
    