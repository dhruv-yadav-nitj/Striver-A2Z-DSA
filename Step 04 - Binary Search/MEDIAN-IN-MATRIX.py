from typing import List
import bisect


class Solution:
    def median(self, matrix: List[List[int]], R: int, C: int) -> int:
        low, high = float('inf'), float('-inf')

        # Find the minimum and maximum elements in the matrix
        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C - 1])

        while low <= high:
            mid = low + (high - low) // 2
            count = 0

            # Count elements less than or equal to mid
            for i in range(R):
                count += bisect.bisect_right(matrix[i], mid)

            if count <= (R * C) // 2:
                low = mid + 1
            else:
                high = mid - 1

        return low
