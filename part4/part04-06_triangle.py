def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
 
def triangle(size):
    i = 0
    while i <= size:
        line(i,"#")
        i += 1
 
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
 