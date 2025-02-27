def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "") 
            parts = line.split(";")  
            fruit = parts[0] 
            price = float(parts[1])  
            fruits_dict[fruit] = price  
            
    return fruits_dict

if __name__ == "__main__":
    print(read_fruits())


