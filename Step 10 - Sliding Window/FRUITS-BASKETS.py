from typing import List
from collections import defaultdict

# SIMILAR TO MAX CONSECUTIVE ONES


class Solution:
    def sumSubarrayMins(self, n: int, fruits: List[int]):
        k = 2  # baskets
        ans = i = j = 0
        n = len(fruits)
        mp = defaultdict(int)
        while j < n:
            mp[fruits[j]] += 1
            if len(mp) > k:
                ans = max(ans, j - i)
                while i < j and len(mp) > k:
                    mp[fruits[i]] -= 1
                    if mp[fruits[i]] == 0:
                        mp.pop(fruits[i])
                    i += 1
            j += 1
        ans = max(ans, j-i)
        return ans
