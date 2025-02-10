def even_numbers(a_list):
    even_list = []
    for i in a_list:
        if i % 2 != 0:
           continue
        even_list.append(i)
    return even_list