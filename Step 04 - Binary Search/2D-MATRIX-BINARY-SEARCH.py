from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if target <= matrix[mid][m - 1]:
                if target >= matrix[mid][0]:
                    ind = bisect.bisect_left(matrix[mid], target)
                    print(mid, ind)
                    return 0 <= ind < m and matrix[mid][ind] == target
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return False
