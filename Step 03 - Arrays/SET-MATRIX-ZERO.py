from typing import List
from collections import defaultdict


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        i = j = col0 = 0
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    if i != 0:
                        matrix[0][j] = matrix[i][0] = 0
                    else:
                        col0 = 1
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0
        if col0:
            for j in range(m):
                matrix[0][j] = 0
