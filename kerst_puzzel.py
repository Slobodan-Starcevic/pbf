row0 = ([0, 0, 3], [0, 1, 0], [0, 0, 0], [0, 0, 5])
row1 = ([0, 6, 3], [0, 0, 5], [0, 2, 4], [0, 5, 0], [6, 0, 0])
row2 = ([0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 0, 0], [0, 0, 0], [0, 0, 3])
row3 = ([0, 3, 5], [0, 0, 0], [1, 4, 0], [0, 0, 0], [0, 0, 0], [2, 6, 0], [0, 6, 0])
row4 = ([0, 0, 0], [0, 0, 3], [0, 0, 0], [0, 1, 3], [0, 0, 5], [0, 0, 0])
row5 = ([4, 0, 0], [6, 0, 0], [0, 0, 0], [0, 0, 0], [0, 5, 3])
row6 = ([6, 0, 0], [0, 0, 5], [0, 5, 4], [0, 0, 0])
board = [row0, row1, row2, row3, row4, row5, row6]
flat_board = [item for sublist in board for item in sublist]

x_totals = {
    37: (row0[3][1], row0[3][2], row1[4][1], row1[4][2],
         row2[5][1], row2[5][2], row3[6][1], row3[6][2]),
    43: (row0[2][1], row0[2][2], row1[3][1], row1[3][2],
         row2[4][1], row2[4][2], row3[5][1], row3[5][2], row4[5][1], row4[5][2]),
    47: (row0[1][1], row0[1][2], row1[2][1], row1[2][2], row2[3][1], row2[3][2],
         row3[4][1], row3[4][2], row4[4][1], row4[4][2], row5[4][1], row5[4][2]),
    52: (row0[0][1], row0[0][2], row1[1][1], row1[1][2], row2[2][1], row2[2][2],
         row3[3][1], row3[3][2], row4[3][1], row4[3][2], row5[3][1], row5[3][2], row6[3][1], row6[3][2]),
    60: (row1[0][1], row1[0][2], row2[1][1], row2[1][2], row3[2][1], row3[2][2],
         row4[2][1], row4[2][2], row5[2][1], row5[2][2], row6[2][1], row6[2][2]),
    38: (row2[0][1], row2[0][2], row3[1][1], row3[1][2], row4[1][1], row4[1][2],
         row5[1][1], row5[1][2], row6[1][1], row6[1][2]),
    39: (row3[0][1], row3[0][2], row4[0][1], row4[0][2],
         row5[0][1], row5[0][2], row6[0][1], row6[0][2]),
}

y_totals = {
    29: (row0[0][0], row0[0][1], row1[0][0], row1[0][1],
         row2[0][0], row2[0][1], row3[0][0], row3[0][1]),
    30: (row0[1][0], row0[1][1], row1[1][0], row1[1][1],
         row2[1][0], row2[1][1], row3[1][0], row3[1][1], row4[0][0], row4[0][1]),
    45: (row0[2][0], row0[2][1], row1[2][0], row1[2][1], row2[2][0], row2[2][1],
         row3[2][0], row3[2][1], row4[1][0], row4[1][1], row5[0][0], row5[0][1]),
    65: (row0[3][0], row0[3][1], row1[3][0], row1[3][1], row2[3][0], row2[3][1],
         row3[3][0], row3[3][1], row4[2][0], row4[2][1], row5[1][0], row5[1][1], row6[0][0], row6[0][1]),
    47: (row1[4][0], row1[4][1], row2[4][0], row2[4][1], row3[4][0], row3[4][1],
         row4[3][0], row4[3][1], row5[2][0], row5[2][1], row6[1][0], row6[1][1]),
    33: (row2[5][0], row2[5][1], row3[5][0], row3[5][1], row4[4][0], row4[4][1],
         row5[3][0], row5[3][1], row6[2][0], row6[2][1]),
    24: (row3[6][0], row3[6][1], row4[5][0], row4[5][1],
         row5[4][0], row5[4][1], row6[3][0], row6[3][1]),
}

z_totals = {
    28: (row0[0][0], row0[0][2], row0[1][0], row0[1][2],
         row0[2][0], row0[2][2], row0[3][0], row0[3][2]),
    39: (row1[0][0], row1[0][2], row1[1][0], row1[1][2],
         row1[2][0], row1[2][2], row1[3][0], row1[3][2], row1[4][0], row1[4][2]),
    36: (row2[0][0], row2[0][2], row2[1][0], row2[1][2], row2[2][0], row2[2][2],
         row2[3][0], row2[3][2], row2[4][0], row2[4][2], row2[5][0], row2[5][2]),
    61: (row3[0][0], row3[0][2], row3[1][0], row3[1][2], row3[2][0], row3[2][2],
         row3[3][0], row3[3][2], row3[4][0], row3[4][2], row3[5][0], row3[5][2], row3[6][0], row3[6][2]),
    46: (row4[0][0], row4[0][2], row4[1][0], row4[1][2], row4[2][0], row4[2][2],
         row4[3][0], row4[3][2], row4[4][0], row4[4][2], row4[5][0], row4[5][2]),
    38: (row5[0][0], row5[0][2], row5[1][0], row5[1][2], row5[2][0], row5[2][2],
         row5[3][0], row5[3][2], row5[4][0], row5[4][2]),
    35: (row6[0][0], row6[0][2], row6[1][0], row6[1][2],
         row6[2][0], row6[2][2], row6[3][0], row6[3][2]),
}


def is_valid(board, row, col, char):
    if char in board[row]:
        return False
    
    if char in [board[i][col] for i in range(16)]:
        return False
    
    start_row, start_col = 4 * (row // 4), 4 * (col // 4)
    for i in range(start_row, start_row + 4):
        for j in range(start_col, start_col + 4):
            if board[i][j] == char:
                return False
    
    return True


def solve_game(flat_b):
    for i in flat_b:
        if board[i] == 0:
            for char in input_choices:
                if is_valid(board, i, j, char):
                    board[i][j] = char
                    if solve_game(board):
                        return True
                    board[i][j] = 0
            return False
    return True


def print_board(board):
    for i, row in enumerate(board):
        if i == 0:
            print("\n               ", row)
        elif i == 1:
            print("          ", row)
        elif i == 2:
            print("     ", row)
        elif i == 3:
            print(row)
        elif i == 4:
            print("     ", row)
        elif i == 5:
            print("          ", row)
        elif i == 6:
            print("               ", row)


print("\nDice puzzle:")
print_board(board)
print("\nSolving...\n")
if solve_game(flat_board):
    print("Solution:")
    print_board(board)
else:
    print("No solution found.")


