num = int(input("Please type in a number: "))
flip = 2

while flip <= num or flip - 1 <= num:
    if flip <= num:
        print(f"{flip}")  
    if flip - 1 <= num:
        print(f"{flip - 1}")
    flip += 2
