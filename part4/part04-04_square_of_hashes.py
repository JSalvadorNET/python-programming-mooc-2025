def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
        
def square_of_hashes(size):
    i = 0
    while i < size:
        line(size,"#")
        i += 1
 
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)