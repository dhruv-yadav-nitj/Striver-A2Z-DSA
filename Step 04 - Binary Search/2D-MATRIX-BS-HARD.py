from typing import List
import bisect


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        cr, cc = 0, m - 1
        while cr < n and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif target > matrix[cr][cc]:
                cr += 1
            else:
                cc -= 1
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        cr, cc = n - 1, 0
        while cr >= 0 and cc < m:
            print(cr, cc)
            if matrix[cr][cc] == target:
                return True
            elif target > matrix[cr][cc]:
                cc += 1
            else:
                cr -= 1
        return False
