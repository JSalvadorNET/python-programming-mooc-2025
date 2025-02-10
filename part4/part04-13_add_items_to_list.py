qtd = int(input("How many items? "))
my_list = []
i = 1
 
while i <= qtd:
    add_num = int(input(f"Item {i}: "))
    my_list.append(add_num)
    i += 1
print(my_list)
    