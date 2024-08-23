from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat = ["." * n for _ in range(n)]
        ans = []

        def isValid(i: int, j: int, board: List[str]):
            if 'Q' in board[i][:j]:
                return False
            ci, cj = i - 1, j - 1
            while ci >= 0 and cj >= 0:
                if board[ci][cj] == 'Q':
                    return False
                ci -= 1
                cj -= 1
            ci, cj = i + 1, j - 1
            while ci < n and cj >= 0:
                if board[ci][cj] == 'Q':
                    return False
                ci += 1
                cj -= 1
            return True

        def helper(ind: int, board: List[str]):
            if ind == n:
                ans.append(board)
                return
            for i in range(n):
                if isValid(i, ind, board):
                    temp = board.copy()
                    temp[i] = temp[i][:ind] + 'Q' + temp[i][ind + 1:]
                    helper(ind + 1, temp)

        helper(0, mat)
        return ans
