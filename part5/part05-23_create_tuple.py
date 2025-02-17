def create_tuple(x: int, y: int, z: int):
    my_tuple = (x,y,z)
    new_tuple = []
    smallest = 0
    greatest = 0
    third_element = x + y + z
    
    if x < y and x < z:
        smallest = x
    elif y < x and y < z:
        smallest = y
    elif z < x and z < y:
        smallest = z
    new_tuple.append(smallest)
    
    if x > y and x > z:
        greatest = x
    elif y > x and y > z:
        greatest = y
    elif z > x and z > y:
        greatest = z
    new_tuple.append(greatest)
    new_tuple.append(third_element)
    
    my_tuple = tuple(new_tuple)
 
    return my_tuple
    
    
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
 