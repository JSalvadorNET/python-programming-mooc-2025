def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    # Check if the coordinates are valid
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    
    # Check if the square is empty
    if game_board[y][x] == "":
        # Place the symbol in the specified position
        game_board[y][x] = piece
        return True
    else:
        # If the square is not empty, return False
        return False
 
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))  # Should print True
    print(game_board)  # Should print [['', '', 'X'], ['', '', ''], ['', '', '']]
 