my_list = []
 
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    my_list.append(item)
    sorted_list = sorted(my_list)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted_list}")