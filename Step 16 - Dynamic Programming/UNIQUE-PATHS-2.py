from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if grid[0][0]:
            return 0

        def tabulation():
            dp = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                if grid[i][0]:
                    break
                dp[i][0] = 1
            for j in range(m):
                if grid[0][j]:
                    break
                dp[0][j] = 1
            for i in range(1, n):
                for j in range(1, m):
                    if grid[i][j]:
                        continue
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            return dp[n - 1][m - 1]

        return tabulation()
