from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        values = mp.values()
        i = j = ans = 0
        n = len(s)
        mp[s[j]] += 1
        while j < n:
            curr = j - i + 1
            max_freq = max(values)
            if curr - max_freq <= k:
                print(i, j)
                ans = max(ans, curr)
                j += 1
                if j < n:
                    mp[s[j]] += 1
            else:
                mp[s[i]] -= 1
                i += 1
        return ans
