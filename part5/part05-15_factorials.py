def factorials(n: int):
    my_dictionary = {}
    num = n
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i 
        my_dictionary[i] = factorial
        i += 1
    return my_dictionary
    
if __name__ == "__main__":
    
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
 