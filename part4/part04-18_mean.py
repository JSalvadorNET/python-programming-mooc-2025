def mean(a_list):
    list_mean = sum(a_list)/len(a_list)
    return list_mean
 
 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(result)
