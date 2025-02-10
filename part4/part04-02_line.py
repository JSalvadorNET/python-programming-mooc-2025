def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
 
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")