x = int(input("Number 1:"))
y = int(input("Number 2:"))
operation = input("Operation:")
 
if operation == "add":
    print(f"\n{x} + {y} = {x + y}")
if operation == "subtract":
    print(f"\n{x} - {y} = {x - y}")
if operation == "multiply":
    print(f"\n{x} * {y} = {x * y}")