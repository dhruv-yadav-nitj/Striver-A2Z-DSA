class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        # tabulation part -> calculate dp array ->
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        ans = ""
        i = n
        j = m
        # string formation part
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                ans += s[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    ans += s[i - 1]
                    i -= 1
                else:
                    ans += t[j - 1]
                    j -= 1
        while i > 0:
            ans += s[i - 1]
            i -= 1
        while j > 0:
            ans += t[j - 1]
            j -= 1
        ans = ans[::-1]
        return ans
