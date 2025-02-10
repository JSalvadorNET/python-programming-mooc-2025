def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
        
def shape(size1, char1, size2, char2):
    i = 0
    j = 0
    while i <= size1:
        line(i,char1)
        i += 1
    while j < size2:
        line(size1,char2)
        j += 1
 
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")