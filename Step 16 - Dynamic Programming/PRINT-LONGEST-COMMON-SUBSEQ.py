"""
Prints only one LCS
"""


class Solution1:
    def all_longest_common_subsequences(self, s: str, t: str):
        n = len(s)
        m = len(t)

        def helper():
            dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp

        res = helper()
        i, j = n, m
        ans = ""
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                ans += s[i - 1]
                i -= 1
                j -= 1
            else:
                if res[i - 1][j] > res[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        ans = ans[::-1]
        return [ans]


"""
Print all the LCS
"""
