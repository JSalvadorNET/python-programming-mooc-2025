def everything_reversed(a_list):
    reversed_word  = ""
    reversed_list = []
    
    for word in a_list:
        reversed_word  = word[::-1]
        reversed_list.append(reversed_word)
    return reversed_list[::-1]
        
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    