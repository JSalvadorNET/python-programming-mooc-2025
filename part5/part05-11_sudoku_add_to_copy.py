def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row[:] for row in sudoku]  
    new_sudoku[row_no][column_no] = number
    return new_sudoku
 
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
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
 
    # Chama a função para adicionar o número
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
 
    # Exibe a grade original e a cópia
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)