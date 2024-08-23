from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        ans = i = 0
        count = defaultdict(int)
        for j in range(n):
            count[s[j]] += 1
            while i < j and count[s[j]] > 1:
                count[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
