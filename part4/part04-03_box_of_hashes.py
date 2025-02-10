def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
 
 
def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1
 
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)