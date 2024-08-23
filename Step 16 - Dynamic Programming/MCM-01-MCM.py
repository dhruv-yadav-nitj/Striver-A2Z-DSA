import sys
from typing import List


class Solution:
    def matrixMultiplication(self, n: int, arr: List[int]):
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def memo(i: int, j: int) -> int:
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            res = sys.maxsize
            for k in range(i, j):
                steps = (arr[i - 1] * arr[k] * arr[j]) + memo(i, k) + memo(k + 1, j)
                res = min(steps, res)
            dp[i][j] = res
            return res

        return memo(1, n - 1)
