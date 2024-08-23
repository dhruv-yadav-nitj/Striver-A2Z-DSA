import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        lim = sys.maxsize
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def memo(i: int, j: int) -> int:
            if i >= n or j >= m:
                return lim
            if (i, j) == (n - 1, m - 1):
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            down = grid[i][j] + memo(i + 1, j)
            right = grid[i][j] + memo(i, j + 1)
            dp[i][j] = min(down, right)
            return dp[i][j]

        def tabulation():
            dpp = [[0 for _ in range(m)] for _ in range(n)]
            dpp[0][0] = grid[0][0]
            for i in range(1, n):
                dpp[i][0] = grid[i][0] + dpp[i - 1][0]
            for j in range(1, m):
                dpp[0][j] = grid[0][j] + dpp[0][j - 1]
            for i in range(1, n):
                for j in range(1, m):
                    dpp[i][j] = grid[i][j] + min(dpp[i - 1][j], dpp[i][j - 1])
            return dpp[n - 1][m - 1]

        return tabulation()
