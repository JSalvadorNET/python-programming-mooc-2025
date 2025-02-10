def sum_of_positives(my_list):
    sum_list = 0
    for i in my_list:
        if i < 0:
           continue
        sum_list += i
    return sum_list
        