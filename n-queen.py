def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0: 
            break
        if board[i][j]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):  
            break
        if board[i][j]:
            return False
    return True

def solve_n_queens_util(board, row):
    if row >= len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  
            solve_n_queens_util(board, row + 1)  
            board[row][col] = False 

def solve_n_queens(n):
    board = [[False] * n for _ in range(n)] 
    solve_n_queens_util(board, 0)

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solve_n_queens(n)
