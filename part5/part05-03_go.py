def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for piece in row:
            if piece == 1:
                player1 += 1
            elif piece == 2:
                player2 += 1
            else:
                continue
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
 
    
    if __name__ == "__main__":
        chess = [
        [1, 2, 2],
        [1, 1, 2],
        [1, 2, 1]
    ]
    print(who_won(chess)) # player 1 won
    chess = [
        [2, 2, 2],
        [1, 1, 2],
        [1, 2, 1]
    ]
    print(who_won(chess)) # player 2 won
    chess = [
        [0, 2, 2],
        [1, 1, 2],
        [1, 2, 1]
    ]
    print(who_won(chess)) # tie
 