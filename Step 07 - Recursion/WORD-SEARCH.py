from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        size = len(word)

        def isValid(ni: int, nj: int):
            return 0 <= ni < n and 0 <= nj < m

        def helper(ind: int, i: int, j: int) -> bool:
            if ind == size:  # base condition
                return True
            if not isValid(i, j) or board[i][j] != word[ind]:
                return False
            row = [-1, 0, 1, 0]
            col = [0, 1, 0, -1]
            temp = board[i][j]
            board[i][j] = '#'
            for k in range(4):
                ni, nj = i + row[k], j + col[k]
                if helper(ind + 1, ni, nj):
                    return True
            board[i][j] = temp
            return False

        for i in range(n):
            for j in range(m):
                if helper(0, i, j):
                    return True
        return False
