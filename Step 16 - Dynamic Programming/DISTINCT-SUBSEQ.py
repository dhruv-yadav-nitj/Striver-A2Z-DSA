class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def memo(i: int, j: int) -> int:
            if j >= m:
                return 1
            if i >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            if s[i] == t[j]:
                pick = memo(i + 1, j + 1)
                notPick = memo(i + 1, j)
                res = pick + notPick
            else:
                res = memo(i + 1, j)
            dp[i][j] = res
            return res

        return memo(0, 0)
