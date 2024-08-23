class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'z': 0
        }
        ans = 0
        s = [c for c in s]
        for i in range(1, len(s)):
            if mp[s[i - 1]] < mp[s[i]] and mp[s[i - 1]] != 0:
                ans += mp[s[i]] - mp[s[i - 1]]
                s[i] = 'z'
            else:
                ans += mp[s[i - 1]]
        ans += mp[s[-1]]
        return ans
