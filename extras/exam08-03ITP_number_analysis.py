my_list = []
most_common = 0
max_count = 0

while True:
    try:
        num = input("Type in a number: ").strip()
        if num == "":
            print("Invalid input! Please enter a valid integer.")
            continue
        num = int(num)  
        if num == 0:
            break
        my_list.append(num)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if not my_list:
    print("No numbers were entered.")
else:
    my_list.sort()

    for num in my_list:
        if my_list.count(num) > max_count:
            most_common = num
            max_count = my_list.count(num)

    print(f"Biggest: {my_list[-1]}")
    print(f"Smallest: {my_list[0]}")
    print(f"Number of numbers: {len(my_list)}")
    print(f"Sum: {sum(my_list)}")
    print(f"Most repeated: {most_common}")
