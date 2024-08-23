"""
Similar to DP on LIS, here also tabulation approach would be more intuitive and helpful in solving other problems!
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def tabulation():
            dpp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dpp[i][j] = 1 + dpp[i - 1][j - 1]
                    else:
                        dpp[i][j] = max(dpp[i - 1][j], dpp[i][j - 1])
            return dpp[n][m]

        def memoization(i: int, j: int) -> int:
            if i >= n or j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            not_pick = pick = 0
            if text1[i] == text2[j]:
                pick = 1 + memoization(i + 1, j + 1)
            else:
                case1 = 0 + memoization(i + 1, j)
                case2 = 0 + memoization(i, j + 1)
                not_pick = max(case1, case2)
            dp[i][j] = max(pick, not_pick)
            return dp[i][j]

        return tabulation()
