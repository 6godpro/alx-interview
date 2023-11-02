#!/usr/bin/python3
"""
The program print every possible solution to the NQueens
problem given a size 'N'
"""
from sys import argv, exit

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = argv[1]

try:
    N = int(N)
except Exception:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

outcomes = []


def isSafe(board, row, col):
    """Validates a given position on the board."""

    for i in range(col):  # to the right
        if board[row][i] == 'Q':
            return False

    # to the left bottom diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # to the left upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve(board, row, col):
    """Returns all possible solutions of the NQueens problem of size N."""
    if col == N:
        tmp = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 'Q':
                    tmp.append([r, c])
        outcomes.append(tmp)

    for i in range(N):
        if isSafe(board, i, row):
            board[i][row] = 'Q'

            if solve(board, row+1, col+1):
                return True

            board[i][row] = 0

    return False


def main():
    """Driver function."""
    board = [[0 for i in range(N)] for i in range(N)]

    solve(board, 0, 0)
    for row in sorted(outcomes):
        print(row)


main()
