import sys
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def memo(i: int, j: int) -> int:
            if j >= m:
                return sys.maxsize
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            op1 = triangle[i][j] + memo(i + 1, j)
            op2 = triangle[i][j] + memo(i + 1, j + 1)
            dp[i][j] = min(op1, op2)
            return dp[i][j]

        def tabulation():
            dpp = [[sys.maxsize for _ in range(m + 1)] for _ in range(n)]
            dpp[0][1] = triangle[0][0]
            for i in range(1, n):
                for j in range(1, i+2):
                    print(i, j)
                    dpp[i][j] = triangle[i][j-1] + min(dpp[i - 1][j - 1], dpp[i - 1][j])
            return min(dpp[-1])

        return tabulation()
