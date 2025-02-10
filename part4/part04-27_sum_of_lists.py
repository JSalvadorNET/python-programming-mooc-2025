def list_sum(list_a,list_b):
    list_c = []  
    for i in range(len(list_a)): 
        list_c.append(list_a[i] + list_b[i])  
        i+= 1
    return list_c
 
if __name__ == "__main__":  
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))


