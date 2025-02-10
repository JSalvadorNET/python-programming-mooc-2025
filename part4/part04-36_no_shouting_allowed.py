def no_shouting(a_list):
    no_upper_list = []
    for i in a_list:
        is_it_upper = i.isupper()
        if is_it_upper == True:
            continue
        else:
            no_upper_list.append(i)
    return no_upper_list
                
 
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)

