class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def memo(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            if s[i] == t[j]:
                res = memo(i - 1, j - 1)
            else:
                res = min(memo(i, j - 1), memo(i - 1, j), memo(i - 1, j - 1))  # insert, delete, replace
            dp[i][j] = res
            return res

        return memo(n - 1, m - 1)
