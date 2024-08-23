from typing import List


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        dummy = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ni, nj = j, n - 1 - i
                dummy[ni][nj] = matrix[i][j]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = dummy[i][j]

# OPTIMISED SOLUTION
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
