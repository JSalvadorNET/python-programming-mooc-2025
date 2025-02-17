def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    block_validator = []  
 
    # Percorre as 3 linhas do bloco
    for i in range(row_no, row_no + 3):
        # Percorre as 3 colunas do bloco
        for j in range(column_no, column_no + 3):
            number = sudoku[i][j]  # Obtém o número na posição atual
            
            if number != 0: 
                if number in block_validator:  
                    return False
                block_validator.append(number)  
    
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
 
    print(block_correct(sudoku, 0,0)) # True
    print(block_correct(sudoku, 1,2)) # False