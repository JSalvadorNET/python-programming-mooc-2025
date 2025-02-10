def formatted(a_list):
    formatted_num = ""
    formatted_list = []
    for num in a_list:
        formatted_num = f"{num:.2f}"
        formatted_list.append(formatted_num)
    return formatted_list
        
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)