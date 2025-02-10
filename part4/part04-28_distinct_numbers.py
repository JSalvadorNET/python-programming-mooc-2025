def distinct_numbers(a_list):
    a_list.sort()  
    distinct_list = [a_list[0]]  
 
    for i in range(1, len(a_list)):  
        if a_list[i] != a_list[i - 1]:  
            distinct_list.append(a_list[i])  
 
    return distinct_list
 
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]