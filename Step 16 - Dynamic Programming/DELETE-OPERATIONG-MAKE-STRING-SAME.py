"""
Followed Up From: MIN-INSERTIONS-TO-MAKE-STRING-PALINDROME
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(s1: str, s2: str) -> int:
            n = len(s1)
            m = len(s2)
            dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[n][m]

        rem = lcs(word1, word2)
        ans = len(word1) + len(word2) - 2 * rem
        return ans
