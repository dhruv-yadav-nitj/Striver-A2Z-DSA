from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        pref, count = 0, 0
        mp[0] = 1
        for item in nums:
            pref += item
            if (pref - k) in mp:
                count += mp[pref-k]
            mp[pref] += 1
        return count

