def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    solve([-1] * n, 0)
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for row in range(n):
            print(' '.join('1' if col == sol[row] else '0' for col in range(n)))
        print()

# Example usage:
n = int(input("Enter the number of queens: "))
print_solutions(solve_n_queens(n), n)