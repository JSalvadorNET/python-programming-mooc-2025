num = int(input("Please type in a positive integer: "))
negative = num*-1
 
for i in range(negative,num+1):
    if i == 0:
        continue
    print(i)