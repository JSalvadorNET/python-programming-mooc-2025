attempts = 0

while True:
    pin = int(input("PIN: "))
    if pin == 4321:
        attempts += 1
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        print("Wrong")
        attempts += 1
