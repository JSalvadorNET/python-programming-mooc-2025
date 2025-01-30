from math import sqrt

while True:
    num = int(input("Please type in a number (0 to exit): "))
    
    if num == 0:
        print("Exiting...")
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(float(sqrt(num)))