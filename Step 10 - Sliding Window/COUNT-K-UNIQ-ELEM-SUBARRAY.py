from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def helper(count: int) -> int:
            i = j = ans = 0
            mp = defaultdict(int)
            while j < n:
                mp[nums[j]] += 1
                while len(mp) > count:
                    mp[nums[i]] -= 1
                    if mp[nums[i]] == 0:
                        mp.pop(nums[i])
                    i += 1
                ans += j - i + 1
                j += 1
            return ans

        return helper(k) - helper(k - 1)
