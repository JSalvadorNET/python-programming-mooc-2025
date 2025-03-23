from fractions import Fraction

def fraction_calculator(calculation: str):
    parts = calculation.split()

    if len(parts) == 1:
        result = Fraction(parts[0])  
    elif len(parts) == 3:

        frac1 = Fraction(parts[0])
        frac2 = Fraction(parts[2])
    
        if parts[1] == "+":
            result = frac1 + frac2
        elif parts[1] == "-":
            result = frac1 - frac2
        elif parts[1] == "*":
            result = frac1 * frac2
        else:
            raise ValueError("Invalid or unknown calculation")
        
    return str(result)
        

def convert_to_fraction(fraction: str):
    return Fraction(fraction)
    

