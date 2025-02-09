def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:  
            print(("10" * size)[:size])
        else:  
            print(("01" * size)[:size])
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
