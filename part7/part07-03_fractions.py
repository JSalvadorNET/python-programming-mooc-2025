from fractions import Fraction

def fractionate(amount: int):
    fraction = Fraction(1, amount) 
    fractions_list = []  
    
    for num in range(amount):  
        fractions_list.append(fraction)  
    
    return fractions_list  

    
if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))