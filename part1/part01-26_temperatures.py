f_degrees = float(input("Please type in a temperature (F):"))
c_degrees = (f_degrees - 32) / 1.8
 
if c_degrees < 0:
    print(f"{f_degrees:.0f} degrees Fahrenheit equals {c_degrees} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{f_degrees:.0f} degrees Fahrenheit equals {c_degrees} degrees Celsius")
 
 
