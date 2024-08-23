# Hint: Using LPS Table used in KMP Algorithm!
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        i = 1
        j = 0
        lps = [0 for _ in range(n)]
        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        return s[-lps[n-1]:] if lps[-1] else ""