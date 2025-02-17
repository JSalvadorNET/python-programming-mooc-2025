def dict_of_numbers():
    singles = {0:"zero", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    composites = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    numbers = {}
    
    for i in range(10):
        numbers[i] = singles[i]
        
    # special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"
    
    for i in range(2,10):
        numbers[i*10] = composites[i]
        for j in range(1,10):
            numbers[i*10+j] = composites[i] + "-" + singles[j]
    
    return numbers
 
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[20])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
 