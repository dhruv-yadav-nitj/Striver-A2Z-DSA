from collections import defaultdict


# Hint: Count Sub-arrays with K different integers (Sliding Window Problem)


class Solution1:
    def substrCount(self, s: str, k: int) -> int:
        # BRUTE FORCE
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                st = set(s[i:j + 1])
                if len(st) == k:
                    ans += 1
        return ans


class Solution:
    def substrCount(self, s: str, k: int) -> int:
        return self.helper(s, k) - self.helper(s, k - 1)

    def helper(self, s: str, k: int) -> int:
        ans = i = j = 0
        n = len(s)
        mp = defaultdict(int)
        while j < n:
            mp[s[j]] += 1
            while len(mp) > k:
                mp[s[i]] -= 1
                if not mp[s[i]]:
                    mp.pop(s[i])
                i += 1
            ans += j - i + 1
            j += 1
        return ans
