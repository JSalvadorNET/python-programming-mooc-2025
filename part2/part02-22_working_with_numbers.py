print("Please type in integer numbers. Type in 0 to finish.")
total_numbers = 0
sum = 0
positive = 0
negative = 0

while True:
    num = int(input("Number: "))
    total_numbers += 1
    sum += num
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        print(f"Numbers typed in {total_numbers - 1}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {sum/(total_numbers-1)}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")
        break