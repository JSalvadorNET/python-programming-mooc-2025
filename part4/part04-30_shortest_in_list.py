def shortest(a_list):
    shortest = a_list[0]
    for word in a_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest
 
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
