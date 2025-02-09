text = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

# Encontrar a primeira ocorrência
first_index = text.find(substring)

if first_index == -1:
    print("The substring does not occur twice in the string. ")
else:
    # Procurar a segunda ocorrência a partir do índice first_index + len(substring)
    second_index = text.find(substring, first_index + len(substring))
    
    if second_index == -1:
        print("The substring does not occur twice in the string. ")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
