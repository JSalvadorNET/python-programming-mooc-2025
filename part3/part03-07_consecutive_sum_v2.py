num = int(input("Limit: "))
i = 1
total_sum = 0
calculation = ""

while total_sum < num:
    if calculation:
        calculation += " + "
    calculation += str(i)
    total_sum += i
    i += 1

print(f"The consecutive sum: {calculation} = {total_sum}")



