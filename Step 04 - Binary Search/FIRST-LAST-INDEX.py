import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # we can either use binary search -> two times -> first to find the first pos and then the last pos
        # else we can use bisect
        last = bisect.bisect_right(nums, target)
        first = bisect.bisect_left(nums, target)
        # case 1 : target exists
        if first < len(nums) and nums[first] == target and last - 1 >= 0 and nums[last - 1] == target:
            return [first, last - 1]
        # case 2 : does not exist
        else:
            return [-1, -1]
