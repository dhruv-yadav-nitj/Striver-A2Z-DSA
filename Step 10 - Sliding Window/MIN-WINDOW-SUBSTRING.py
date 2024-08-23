from collections import defaultdict, Counter
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m > n:
            return ""
        mp = defaultdict(int, Counter(t))
        count = m
        size = sys.maxsize
        start = i = j = 0
        while j < n:
            if s[j] in mp and mp[s[j]] > 0:
                count -= 1
            mp[s[j]] -= 1
            while count == 0:
                if j - i + 1 < size:
                    size = j - i + 1
                    start = i
                mp[s[i]] += 1
                if mp[s[i]] > 0:
                    count += 1
                i += 1
            j += 1
        if size != sys.maxsize:
            return s[start:start+size]
        else:
            return ""
