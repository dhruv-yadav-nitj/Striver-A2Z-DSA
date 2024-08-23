from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def compare(s: str, t: str) -> bool:
            n = len(s)  # suc
            m = len(t)  # pre
            if n - m != 1:
                return False
            i = j = 0
            while i < n and j < m:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if (j == m and i == n) or (j == m and i + 1 == n):
                return True
            else:
                return False

        n = len(words)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if compare(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
