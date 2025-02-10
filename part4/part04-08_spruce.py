def spruce(size):
    print("a spruce!")
    i = 0
    while i < size:
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
        i += 1
    print(" " * (size - 1) + "*")
 
 
'''
#Complicated version 1
 
def spruce(size):
    row = "*"
    n = size-1
    print("a spruce!")
    while n+1 > 0:
        print(" " * n + row)
        row += "**"
        n -= 1
    n = size-1
    row = "*"
    print(" " * n + row)
'''
 
if __name__ == "__main__":
    spruce(5)
    
    
    
    
 