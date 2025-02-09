num = int(input("Please type in a number: "))
x = 1

while x <= num:
    y = 1
    while y <= num:
        result = x*y
        print(f"{x} x {y} = {result}")
        y += 1   
    x +=1
