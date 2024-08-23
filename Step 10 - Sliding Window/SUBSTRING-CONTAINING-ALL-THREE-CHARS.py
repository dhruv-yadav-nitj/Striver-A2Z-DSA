from collections import defaultdict


class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 2):
            mp = defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                if len(mp) >= 3:
                    count += 1
        return count


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 2):
            mp = defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                if len(mp) >= 3:
                    count += (n - j)
                    break
        return count


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = i = j = 0
        mp = defaultdict(int)
        while j < n:
            mp[s[j]] += 1
            while len(mp) >= 3:
                ans += (n - j)
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    mp.pop(s[i])
                i += 1
            j += 1
        return ans
