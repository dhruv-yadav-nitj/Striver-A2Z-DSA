from typing import List


class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = mat[i][0]
        for j in range(m):
            dp[0][j] = mat[0][j]
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j]:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += dp[i][j]
        return ans
