#!/usr/bin/python3
"""
N Queens puzzle solution
Usage: nqueens N
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in a given position.
    """
    # Check the column on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n):
    """
    Recursive utility function to solve N Queens problem.
    """
    if col >= n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n)
            board[i][col] = 0


def print_solution(board, n):
    """
    Print the N Queens solution.
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def nqueens(n):
    """
    Main function to solve the N Queens problem.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
