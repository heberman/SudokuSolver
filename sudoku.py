def main():
    board = [
        [0, 6, 0, 0, 0, 0, 7, 5, 0],
        [0, 0, 0, 0, 3, 6, 8, 0, 0],
        [0, 0, 2, 8, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [9, 0, 8, 0, 0, 0, 1, 0, 7],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 4, 2, 0, 0],
        [0, 0, 3, 6, 1, 0, 0, 0, 0],
        [0, 7, 9, 0, 0, 0, 0, 8, 0]
    ]

    # build set of cells that can't be changed
    locked_cells = []
    for i in range(81):
        if board[i // 9][i % 9] != 0:
            locked_cells.append(i)

    # build the sets of cells that are in each 3 x 3 square
    squares = []
    for m in range(3):
        for n in range(3):
            square_cells = []
            for o in range(0, 27, 9):
                for p in range(3):
                    square_cells.append(((m * 3) + o + p) + n * 27)
            squares.append(square_cells)

    # run algorithm
    x = 0
    backtrack_val = 0
    while x < 81:
        if x in locked_cells:
            x += 1
            continue
        row = x // 9
        column = x % 9
        for i in range(backtrack_val + 1, 10):
            board[row][column] = i
            if check_valid(board, squares):
                x += 1
                backtrack_val = 0
                break
        else:
            # no valid values found for cell x so now backtrack
            while board[row][column] == 9:
                board[row][column] = 0
                x -= 1
                while x in locked_cells:
                    x -= 1
                if x < 0:
                    print("exiting")
                    exit()
                row = x // 9
                column = x % 9
            backtrack_val = board[row][column]

    print("\n---Solution---\n")
    for row in board:
        print(row)

    return 0


def check_rows(board):
    for row in board:
        for x in range(len(row)):
            for i in range(1, 9 - x):
                if row[x] == row[x + i] and row[x] != 0:
                    return False

    return True


def check_columns(board):
    for a in range(9):
        column = []
        for row in board:
            column.append(row[a])
        for x in range(9):
            for i in range(1, 9 - x):
                if column[x] == column[x + i] and column[x] != 0:
                    return False
    return True


def check_squares(board, squares):
    for square in squares:
        seen = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for cell in square:
            row = cell // 9
            column = cell % 9
            if board[row][column] == 0:
                continue
            if seen[board[row][column]] == 0:
                seen[board[row][column]] = 1
            else:
                return False
    return True


def check_valid(board, squares):
    return check_rows(board) and check_columns(board) and check_squares(board, squares)


if __name__ == '__main__':
    main()
