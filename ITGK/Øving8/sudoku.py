def make_board(board_string):
    board = []
    for i in range(5):
        board.append(list(board_string[i*5:(i+1)*5]))
    return board

def print_board(board):
    def print_horizontal_border():
        print("  +---+---+---+---+---+")

    print("    0   1   2   3   4")
    print_horizontal_border()
    for i, row in enumerate(board):
        print(f"{i} | " + " | ".join(row) + " |")
        print_horizontal_border()


def get_piece(board, row, col):
    return board[row][col]


def get_legal_moves(board, row, col):
    piece = board[row][col]
    if piece.upper() == 'P':
        return get_pawn_moves(board, row, col)
    elif piece.upper() == 'R':
        return get_rook_moves(board, row, col)
    elif piece.upper() == 'N':
        return get_knight_moves(board, row, col)
    elif piece.upper() == 'B':
        return get_bishop_moves(board, row, col)
    elif piece.upper() == 'Q':
        return get_queen_moves(board, row, col)
    elif piece.upper() == 'K':
        return get_king_moves(board, row, col)
    else:
        return []

def get_pawn_moves(board, row, col):
    moves = []
    piece = board[row][col]
    direction = -1 if piece.isupper() else 1  
    
    if 0 <= row + direction < 5 and board[row + direction][col] == '.':
        moves.append((row + direction, col))
    

    for dc in [-1, 1]:
        if 0 <= row + direction < 5 and 0 <= col + dc < 5:
            target = board[row + direction][col + dc]
            if target != '.' and target.isupper() != piece.isupper():
                moves.append((row + direction, col + dc))
    
    return moves

def get_rook_moves(board, row, col):
    moves = []
    piece = board[row][col]
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for step in range(1, 5):
            new_row, new_col = row + direction[0] * step, col + direction[1] * step
            if 0 <= new_row < 5 and 0 <= new_col < 5:
                target = board[new_row][new_col]
                if target == '.':
                    moves.append((new_row, new_col))
                elif target.isupper() != piece.isupper():
                    moves.append((new_row, new_col))
                    break
                else:
                    break
            else:
                break
    
    return moves

def get_knight_moves(board, row, col):
    moves = []
    piece = board[row][col]


    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 5 and 0 <= new_col < 5:
            target = board[new_row][new_col]
            if target == '.' or target.isupper() != piece.isupper():
                moves.append((new_row, new_col))
    
    return moves

def get_bishop_moves(board, row, col):
    moves = []
    piece = board[row][col]


    for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for step in range(1, 5):
            new_row, new_col = row + direction[0] * step, col + direction[1] * step
            if 0 <= new_row < 5 and 0 <= new_col < 5:
                target = board[new_row][new_col]
                if target == '.':
                    moves.append((new_row, new_col))
                elif target.isupper() != piece.isupper():
                    moves.append((new_row, new_col))
                    break
                else:
                    break
            else:
                break
    
    return moves

def get_queen_moves(board, row, col):
    return get_rook_moves(board, row, col) + get_bishop_moves(board, row, col)

def get_king_moves(board, row, col):
    moves = []
    piece = board[row][col]


    king_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for move in king_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 5 and 0 <= new_col < 5:
            target = board[new_row][new_col]
            if target == '.' or target.isupper() != piece.isupper():
                moves.append((new_row, new_col))
    
    return moves

board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)

print_board(board)
print(get_legal_moves(board, 2, 2))

