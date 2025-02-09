i = 1
line = "-"

while i == 1:
    string = input("Please type in a string: ")
    if string == "":
        i = 0
    print(f"{string}")
    print(f"{line*len(string)}")