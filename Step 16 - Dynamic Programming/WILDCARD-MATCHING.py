class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def memo(i: int, j: int) -> bool:
            if i < 0:
                if j < 0:  # both s and t exhausted
                    return True
                else:  # s exhausted but t rem
                    while j >= 0:
                        if p[j] != '*':
                            return False
                        j -= 1
                    return True
            if j < 0 <= i:  # t exhausted but s rem
                return False
            if dp[i][j] != -1:
                return bool(dp[i][j])
            res = None
            if s[i] == p[j] or p[j] == '?':
                res = memo(i - 1, j - 1)
            else:
                if p[j] == '*':
                    res = memo(i - 1, j) or memo(i, j - 1) or memo(i - 1, j - 1)
                else:
                    res = False
            dp[i][j] = res
            return res

        return memo(n - 1, m - 1)
