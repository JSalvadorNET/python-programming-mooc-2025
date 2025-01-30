num = int(input("Number: "))

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    None