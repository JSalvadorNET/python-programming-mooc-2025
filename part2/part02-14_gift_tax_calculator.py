gift_value = float(input("Value of gift: "))
 
if gift_value < 5000:
    print("No tax!")
else:
    if 5000 <= gift_value < 25000:
        tax = 100 + (gift_value - 5000) * 0.08
    elif 25000 <= gift_value < 55000:
        tax = 1700 + (gift_value - 25000) * 0.10
    elif 55000 <= gift_value < 200000:
        tax = 4700 + (gift_value - 55000) * 0.12
    elif 200000 <= gift_value < 1000000:
        tax = 22100 + (gift_value - 200000) * 0.15
    else:
        tax = 142100 + (gift_value - 1000000) * 0.17
 
    print(f"Amount of tax: {tax:.1f} euros")