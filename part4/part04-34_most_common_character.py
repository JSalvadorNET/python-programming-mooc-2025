def most_common_character(string):
    max_count = 0
    common_char = ""
    
    for i in string:
        count = string.count(i)
        
        if count > max_count:
            max_count = count
            common_char = i
 
    return common_char
 
        
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
 
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
        