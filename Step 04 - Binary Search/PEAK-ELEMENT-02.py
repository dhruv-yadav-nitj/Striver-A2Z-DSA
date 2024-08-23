from typing import List


# SIMILAR TO PEAK ELEMENT

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            col, maxi = max(enumerate(mat[mid]), key=lambda x: x[1])
            up = -1 if mid == 0 else mat[mid - 1][col]
            right = -1 if col == m - 1 else mat[mid][col + 1]
            down = -1 if mid == n - 1 else mat[mid + 1][col]
            left = -1 if col == 0 else mat[mid][col - 1]
            if maxi > up and maxi > down and maxi > left and maxi > right:
                return [mid, col]
            elif maxi < up:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
