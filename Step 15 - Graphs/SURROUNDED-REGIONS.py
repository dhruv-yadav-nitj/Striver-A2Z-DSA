from typing import List

"""
Initiate those 'O's which are at border of the board and apply dfs from there to mark 'O's which would remain unchanged.
Rest all the cells would be captured in the final board!
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]

        def dfs(i: int, j: int) -> None:
            board[i][j] = -1
            for k in range(4):
                ni = i + row[k]
                nj = j + col[k]
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'O':
                    dfs(ni, nj)

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] != -1:
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
