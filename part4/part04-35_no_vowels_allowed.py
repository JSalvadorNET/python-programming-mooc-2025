def no_vowels(string):
    no_vowel_string = ""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        no_vowel_string += i
    return no_vowel_string
   
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
        
    