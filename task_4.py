def is_valid(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  
                return False  
    return True  
def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def main():
    print("Welcome to Sudoku Solver!")
    print("Please enter the Sudoku puzzle, row by row, using 0 for empty cells.")

    sudoku_board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        sudoku_board.append(row)

    if solve_sudoku(sudoku_board):
        print("\nSudoku Solved:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()