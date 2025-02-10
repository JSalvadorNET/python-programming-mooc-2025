def length_of_longest(a_list):
    longest = 0
    for word in a_list:
        if len(word) > longest:
            longest = len(word)
    return longest
    
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
    my_list = ["Alan", "Grace", "Frances", "Kim", "Susan"]
    result = length_of_longest(my_list)
    print(result)
    