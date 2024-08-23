import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = bisect.bisect_right(nums, target)
        if ind - 1 >= 0 and nums[ind - 1] == target:
            return ind - 1
        else:
            return ind
