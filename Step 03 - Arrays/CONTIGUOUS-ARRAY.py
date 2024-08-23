from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = x = 0
        n, mp = len(nums), defaultdict()
        for i in range(n):
            x = x + 1 if nums[i] else x - 1
            if x == 0:
                ans = max(ans, i+1)
            req = x - 0  # i.e., if x already exists in the mp -> then the subarray b/w mp[x] and i would be having
            # sum = 0 hence equal no. of 0s and 1s
            if req in mp:
                ans = max(ans, i - mp[req])
            if x not in mp:
                mp[x] = i
        return ans
