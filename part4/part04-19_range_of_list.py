def range_of_list(a_list):
    list_sorted = sorted(a_list)
    list_range = list_sorted[-1] - list_sorted[0]
    return list_range
 
 
if __name__ == "__main__":
    my_list = [1, 2, 5, 4, 3]
    result = range_of_list(my_list)
    print(result)