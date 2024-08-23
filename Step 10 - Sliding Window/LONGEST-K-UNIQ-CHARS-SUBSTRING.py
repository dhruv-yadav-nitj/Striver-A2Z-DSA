from collections import defaultdict


class Solution:
    def longestKSubstr(self, s: str, k: int):
        ans, n = -1, len(s)
        # print(n)
        i = j = 0
        mp = defaultdict(int)
        while j < n:
            mp[s[j]] += 1
            while len(mp) > k:
                ans = max(ans, j - i)
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    mp.pop(s[i])
                i += 1
            j += 1
            if len(mp) == k:  # handles the edge case when the last subarray (when j becomes n) is also valid for us
                ans = max(ans, j-i)
        return ans
