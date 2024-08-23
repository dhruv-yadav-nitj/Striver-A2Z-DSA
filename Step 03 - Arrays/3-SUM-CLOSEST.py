from typing import List
from sys import maxsize


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans, dev = None, maxsize
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                print(nums[i], nums[j], nums[k])
                if res == target:
                    return target
                elif res < target:
                    d = abs(target - res)
                    if d < dev:
                        ans, dev = res, d
                    j += 1
                else:
                    d = abs(target - res)
                    if d < dev:
                        ans, dev = res, d
                    k -= 1
        return ans
