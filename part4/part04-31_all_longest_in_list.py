def all_the_longest(a_list):
    max_length = 0
    longest_list = []
    for word in a_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_list = [word]
        elif len(word) == max_length:
            longest_list.append(word)
    return longest_list
 
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)