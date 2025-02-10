# Copy here code of line function from previous exercise
def line(size, charactere):
    if charactere == "":
        print("*"*size)
    else:
        print(charactere[0]*size)
        
def square(size, charactere):
    i = 0
    while i < size:
        line(size,charactere)
        i += 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")