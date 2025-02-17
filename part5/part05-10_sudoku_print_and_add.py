def add_number(sudoku: list, row: int, col: int, num: int):
    if sudoku[row][col] == 0:  
        sudoku[row][col] = num
    else:
        print(f"Erro: position ({row}, {col}) already contains a number.")
 
def print_sudoku(sudoku: list):
    row_count = 0 
    for row in sudoku:
        if row_count > 0 and row_count % 3 == 0:  
            print()
        
        col_count = 0 
        for num in row:
            if col_count > 0 and col_count % 3 == 0:  
                print("", end=" ")
 
            if num == 0:
                print("_", end=" ") 
            else:
                print(num, end=" ")  
            
            col_count += 1  
        
        print()  
        row_count += 1  
 
if __name__ == "__main__":
    sudoku = [[0] * 9 for _ in range(9)]  
 
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
 
    print("\nThree numbers added:\n")
    print_sudoku(sudoku)