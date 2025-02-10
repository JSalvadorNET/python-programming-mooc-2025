my_list = []
i = 1
 
while True:
    print(f"The list is now {my_list}")
    op = input("a(d)d, (r)emove or e(x)it:")
    if op == "x":
        print("Bye!")
        break
    if op == "d":
        my_list.append(i)
        i += 1
    if op == "r":
        if len(my_list) > 1:
            my_list.pop(-1)
            i = my_list[-1]+1
        else:
            my_list = []
            i = 1
        