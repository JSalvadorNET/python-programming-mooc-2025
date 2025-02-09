string = input("Please type in a string: ")
length = int(len(string))
i = -1
length = int(len(string)*-1)

while i != length-1:
    print(f"{string[i]}")
    i -= 1