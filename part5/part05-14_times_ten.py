def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    i = start_index-1
    
    while i != end_index:
        i+= 1
        my_dictionary[i] = i*10
    return my_dictionary
        
if __name__ == "__main__":
    print(times_ten(2,5))
    print(times_ten(3,6))
    print(times_ten(5,15))