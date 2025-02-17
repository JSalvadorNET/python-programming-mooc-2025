def column_correct(sudoku: list, col_no: int) -> bool:
    col_validator = [] 
    
    for row in sudoku:  
        number = row[col_no]  
        if number != 0 and number in col_validator:  
            return False  
        col_validator.append(number) 
    
    return True  
    
 
    if __name__ == "__main__":
            sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
 
    print(row_correct(sudoku, 0)) # False
    print(row_correct(sudoku, 1)) # True