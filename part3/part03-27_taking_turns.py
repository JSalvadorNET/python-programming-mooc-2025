num = int(input("Please type in a number: "))
low = 1
high = num 

while low <= high:
    print(f"{low}")  
    if low != high:  
        print(f"{high}")  
    low += 1  
    high -= 1 
