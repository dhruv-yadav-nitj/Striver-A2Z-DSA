from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9

        def isValid(sud: List[List[str]], row: int, col: int, c: str) -> bool:
            # check same row
            for j in range(n):
                if sud[row][j] == c:
                    return False
            # check same col
            for i in range(n):
                if sud[i][col] == c:
                    return False
            for i in range(n):
                if sud[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == c:
                    return False
            return True

        def helper(sud: List[List[str]]) -> bool:
            for i in range(n):
                for j in range(n):
                    if sud[i][j] == '.':
                        for k in range(1, 10):
                            c = str(k)
                            if isValid(sud, i, j, c):
                                sud[i][j] = c
                                if helper(sud):
                                    return True
                                sud[i][j] = '.'
                        return False
            return True

        helper(board)
