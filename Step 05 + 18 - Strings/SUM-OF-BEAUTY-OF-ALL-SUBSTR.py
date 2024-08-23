from collections import defaultdict


# Time Complexity: O(n^2*26)
class Solution1:
    def beautySum(self, s: str) -> int:
        cnt = 0
        n = len(s)
        for i in range(n):
            mp = defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                maxi = 0
                mini = 501
                for k, v in mp.items():
                    maxi = max(maxi, v)
                    mini = min(mini, v)
                cnt += (maxi - mini)
        return cnt
