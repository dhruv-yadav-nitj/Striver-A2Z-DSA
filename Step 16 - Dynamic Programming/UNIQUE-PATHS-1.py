class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def memoization(i: int, j: int) -> int:
            if (i, j) == (m - 1, n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            down = memoization(i + 1, j)
            right = memoization(i, j + 1)
            dp[i][j] = down + right
            return dp[i][j]

        def tabulation():
            dpp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                dpp[i][0] = 1
            for j in range(n):
                dpp[0][j] = 1
            for i in range(1, m):
                for j in range(1, n):
                    dpp[i][j] = dpp[i - 1][j] + dpp[i][j - 1]
            return dpp[m - 1][n - 1]

        return tabulation()
